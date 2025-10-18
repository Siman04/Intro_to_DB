import mysql.connector
from mysql.connector import Error

def create_database(host, user, password, db_name):
    connection = None
    cursor = None
    
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            db_creation_query = "CREATE DATABASE IF NOT EXISTS {}".format(db_name)
            cursor.execute(db_creation_query)
            
            print(f'Database "{db_name}" created successfully!')
            
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    DB_NAME = "alx_book_store"
    create_database("localhost", "root", "your_password", DB_NAME)