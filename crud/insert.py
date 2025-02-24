# crud/create.py
from db import get_db_connection

def create_user(id, timestamp,  author, sentiments_score, description):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO news (id, timestamp,  author, sentiments_score, description) VALUES (%s, %s, %s, %s, %s);"
            cursor.execute(query, (id, timestamp,  author, sentiments_score, description))
            conn.commit()
            cursor.close()
            print(f"User: {id} created successfully.")
        except Exception as e:
            print(f"Error creating user: {e}")
        finally:
            conn.close()