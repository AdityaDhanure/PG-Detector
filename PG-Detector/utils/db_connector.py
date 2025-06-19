import psycopg2 # It is used to connect to PostgreSQL databases

def try_db_connection(creds):
    try:
        conn = psycopg2.connect(
            host=creds['host'],
            port=creds['port'],
            dbname=creds['dbname'],
            user=creds['user'],
            password=creds['password']
        )
        conn.close()
        return True
    except Exception as e:
        print(f"DB Connection Error: {e}")
        return False
