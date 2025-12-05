import mysql.connector
from mysql.connector import Error

try:
    # Step 1: Connect to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ashu",
        database="login_data"
    )

    if connection.is_connected():
        print("Connected to the database")
    
    # Step 2: Prepare and execute the query
    username = "000105"  # Replace with the username input by the user
    password = "ashu@123"  # Replace with the password input by the user

    query = "SELECT * FROM users WHERE Username = %s AND Pass_Word = %s"
    
    cursor = connection.cursor()
    cursor.execute(query, (username, password))
    
    # Step 3: Fetch the result and check credentials
    result = cursor.fetchone()
    
    if result:
        print("Access Granted")
    else:
        print("Access Denied: Incorrect Username or Password")

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
