import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pratik",
        database="vibeosys"
    )
    if connection.is_connected():
        print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")
finally:
    if connection.is_connected():
        connection.close()
