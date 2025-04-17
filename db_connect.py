import psycopg2

print("👋 Script started!")

# Supabase connection info
HOST = "db.zwbjqaxcaiylwrbnvdns.supabase.co"
DATABASE = "postgres"
USER = "postgres"
PASSWORD = "d+bZeF5.VQNL3rV"
PORT = 5432

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
