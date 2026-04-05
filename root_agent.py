import google.generativeai as genai
import os
from dotenv import load_dotenv
from tools import run_sql_query
import re

def clean_sql(text):
    # Remove markdown code blocks
    text = re.sub(r"```sql", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```", "", text)

    # Remove extra spaces/newlines
    text = text.strip()

    return text

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

SQL_PROMPT = """
You are an expert PostgreSQL assistant.

Database:
Schema: bollywood
Table: movies
Columns:
- id (int)
- title (text)
- year (text but represents numeric values)
- rating (text but represents numeric values)

Task:
Convert the user question into a valid PostgreSQL SQL query.

IMPORTANT RULES:
- Always use full table name: movies
- rating column is TEXT → always CAST it to FLOAT for comparison
  Example: CAST(rating AS FLOAT)
- year column is TEXT → always CAST it to int for comparison
- Use >= or <= instead of strict equality unless explicitly asked
- If user says "top" → ORDER BY CAST(rating AS FLOAT) DESC LIMIT 5
- If no limit mentioned → LIMIT 5
- Only SELECT queries allowed
- Output ONLY SQL (no explanation, no markdown)

Examples:

User: show movies with rating 6
Output: SELECT title, rating FROM movies WHERE CAST(rating AS FLOAT) >= 6 LIMIT 5;

User: movies above 7
Output: SELECT title, rating FROM movies WHERE CAST(rating AS FLOAT) > 7 LIMIT 5;

User: top movies
Output: SELECT title, rating FROM movies ORDER BY CAST(rating AS FLOAT) DESC LIMIT 5;

Now generate SQL:
"""
ANSWER_PROMPT = """
You are a friendly Bollywood movie assistant.

User asked:
{question}

Data retrieved:
{result}

Your job:
- Give a natural, conversational answer
- Mention movie names clearly
- Include ratings if available
- Do NOT mention SQL or technical errors
- If no results → say it naturally (not robotic)

Examples:

Good:
"Here are some Bollywood movies with ratings above 6: Dangal (8.4), 3 Idiots (8.0)..."

Bad:
"I'm sorry, I encountered an issue..."

Now respond:
"""

def root_agent(user_input: str):
    try:
        # Step 1: Generate SQL
        sql_response = model.generate_content(
            SQL_PROMPT + "\nUser: " + user_input
        )
        sql_query = clean_sql(sql_response.text)

        # Step 2: Execute SQL
        result = run_sql_query(sql_query)

        # Step 3: Generate Final Answer
        final_response = model.generate_content(
            ANSWER_PROMPT.format(
                question=user_input,
                query=sql_query,
                result=result
            )
        )

        return {
            "answer": final_response.text.strip(),
            "sql_query": sql_query,   # keep for debugging/demo
            "raw_result": result
        }

    except Exception as e:
        return {"error": str(e)}
