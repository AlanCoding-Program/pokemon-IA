import psycopg
from typing import Generator
import os
from dotenv import load_dotenv

load_dotenv()
password_supabase = os.getenv("password_supabase")

url=f"postgresql://postgres.ctwqgmrlkhfuirnbangi:{password_supabase}@aws-1-us-east-2.pooler.supabase.com:6543/postgres "


def getCursor() -> Generator[psycopg.Cursor, None, None]:
    conn = psycopg.connect(url,sslmode="require")
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()