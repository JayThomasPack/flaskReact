import psycopg2
from config import Config

def save_questionnaire(url, questionnaire):
    conn = psycopg2.connect(
        dbname=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        host=Config.DB_HOST
    )
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO questionnaires (url, data)
            VALUES (%s, %s)
            ON CONFLICT (url) DO UPDATE SET data = EXCLUDED.data
        """, (url, questionnaire))
        conn.commit()
    conn.close()
