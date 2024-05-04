import mysql.connector
import bcrypt
import logging

connection = None

def connectToSQL():
    # Create a connection to the MySQL database
    conn = mysql.connector.connect(
        host='localhost',
        user='kurir',
        password='kurir',
        database='tpo24'
    )
    return conn

def  connectionEstablished():
        return connection is None

def writeUserToDb(username: str, password: str, accountType: str):
    # create a new cursor object, which is used to execute SQL commands, and define a SQL query
    cursor = connection.cursor()
    # Check if the username already exists in the database
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchall()
    if result:
        return False
    query = "INSERT INTO users (username, password_hash, acc_type) VALUES (%s, %s, %s)"
    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    cursor.execute(query, (username, hashed_password, accountType))
    connection.commit()
    cursor.close()
    return True

def validateLogin(username: str, password: str):
    # create a new cursor object, which is used to execute SQL commands, and define a SQL query
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE username = %s"
    # execute the query
    cursor.execute(query, (username,))
    result = cursor.fetchall()
    cursor.close()

    #### FIX THIS
        # If user not found, db returns empty tuple
    if not result:
        return False, result, 404

    # Check if the hashed password matches the one in the database
    if bcrypt.checkpw(password.encode('utf-8'), result[0][2].encode('utf-8')):