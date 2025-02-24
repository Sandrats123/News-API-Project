from db import get_db_connection

def get_user(id, timestamp,  author, sentiment_score, description):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM news WHERE id = %s;"
            cursor.execute(query, (id, timestamp,  author, sentiment_score, description))
            user = cursor.fetchone()
            cursor.close()
            if user:
                print(f"User found: {user}")
            else:
                print(f"No user found with ID {timestamp}.")
            
        except Exception as e:
            print(f"Error reading user: {e}")
        finally:
            conn.close()