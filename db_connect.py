import psycopg2
import socket
import os

print("👋 Script started!")

# Force IPv4 — this avoids Render's IPv6 issue
orig_getaddrinfo = socket.getaddrinfo

def getaddrinfo_ipv4(*args, **kwargs):
    return [info for info in orig_getaddrinfo(*args, **kwargs) if info[0] == socket.AF_INET]

socket.getaddrinfo = getaddrinfo_ipv4

# Read connection info from environment variables
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT", 5432))
DATABASE = os.getenv("DATABASE")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

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
