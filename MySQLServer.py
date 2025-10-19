import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update credentials if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='62626262Pl@'  # Add your MySQL password here if you have one
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Always close connection properly
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Optional print to confirm cleanup
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
