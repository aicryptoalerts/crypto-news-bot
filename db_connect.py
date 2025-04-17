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

    # 🔽 INSERT sample news
    cur = conn.cursor()
    print("📢 Attempting insert into Supabase...")
    cur.execute("""
        INSERT INTO news_alerts (headline, source, impact)
        VALUES (%s, %s, %s);
    """, ("US CPI higher than expected", "Twitter", "Negative"))

    conn.commit()
    print("📩 Sample news alert inserted into database!")

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Connection failed or insert error:")
    print(e)
