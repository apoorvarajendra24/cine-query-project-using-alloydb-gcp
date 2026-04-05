FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["streamlit", "run", "adk_agent/streamlit_app.py", "--server.port=8080", "--server.address=0.0.0.0"]
