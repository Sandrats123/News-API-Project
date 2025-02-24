# create_table.py
from db import get_db_connection

def create_users_table():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # Define the CREATE TABLE query
            create_table_query = """
            CREATE TABLE IF NOT EXISTS news (
                id SERIAL PRIMARY KEY,
                timestamp varchar(20),
                author VARCHAR(50),
                sentiments_score FLOAT,
                Description varchar(700)
            );
            """
            cursor.execute(create_table_query)
            conn.commit()
            cursor.close()
            print("news table created successfully or already exists.")
        except Exception as e:
            print(f"Error creating news table: {e}")
        finally:
            conn.close()