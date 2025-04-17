import psycopg2
import os

print("👋 Script started!")

# Load from environment variables
HOST = os.getenv("DB_HOST")
DATABASE = os.getenv("DB_NAME")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
PORT = os.getenv("DB_PORT", 5432)  # fallback to default port 5432

try:
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        database=DATABASE,
        user=USER,
        password=PASSWORD
    )
    print("✅ Connected to Supabase PostgreSQL!")
    conn.close()

except Exception as e:
    print("❌ Connection failed:")
    print(e)
