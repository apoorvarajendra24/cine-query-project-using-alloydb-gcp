import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def run_sql_query(query: str):
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        cursor = conn.cursor()
        cursor.execute(query)

        if query.strip().lower().startswith("select"):
            result = cursor.fetchall()
        else:
            conn.commit()
            result = "Query executed successfully"

        cursor.close()
        conn.close()

        return result

    except Exception as e:
        return str(e)
