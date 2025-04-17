try:
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        database=DATABASE,
        user=USER,
        password=PASSWORD
    )
    print("✅ Connected again for insert.")

    cur = conn.cursor()
    print("📢 Attempting insert into Supabase...")  # <--- NEW LINE

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
