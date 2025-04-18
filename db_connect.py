import psycopg2
import os
import socket

print("👋 Script started!")

# Force IPv4 (this avoids Supabase IPv6 issues on Railway)
original_getaddrinfo = socket.getaddrinfo
def getaddrinfo_ipv4(*args, **kwargs):
    return [info for info in original_getaddrinfo(*args, **kwargs) if info[0] == socket.AF_INET]
socket.getaddrinfo = getaddrinfo_ipv4

# Load connection details from environment variables
HOST = os.getenv("DB_HOST")
DATABASE = os.getenv("DB_NAME")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
PORT = os.getenv("DB_PORT", 5432)  # fallback to 5432 if not defined

try:
    # Connect to Supabase PostgreSQL
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        database=DATABASE,
        user=USER,
        password=PASSWORD
    )
    print("✅ Connected to Supabase PostgreSQL!")

    # Insert a sample news alert
    cur = conn.cursor()
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
