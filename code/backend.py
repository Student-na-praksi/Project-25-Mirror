from flask import Flask, request, jsonify, render_template

import mysql.connector
import bcrypt
import logging

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='kurir',
    password='kurir',
    database='tpo24'
)

# Create a new Flask web server from the Flask class
app = Flask(__name__, static_url_path='/static')
# app will log all the messages which are at the level INFO or above.
app.logger.setLevel(logging.INFO)

# This line sets the configuration for the Flask application to pretty-print JSON output. This makes JSON output easier to read.
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    
# Handle the index page
@app.route('/')
def index():
    return render_template('index.html')

# Log every incoming request
# @app.before_request
# def log_request():
#     app.logger.info('Request received: %s %s', request.method, request.path)

# Handle the register endpoint
@app.route('/register', methods=['POST'])
def register():
    app.logger.info('Register button clicked')

    try:
        # get the JSON data from the request, and then extract the 'username' and 'password' fields.
        data = request.get_json()
        username = data['username']
        password = data['password']
        app.logger.info('Inserting user %s with password %s into DB', username, password)
        
        # create a new cursor object, which is used to execute SQL commands, and define a SQL query
        cursor = connection.cursor()
        # Check if the username already exists in the database
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchall()
        if result:
            app.logger.info('User %s ALREADY EXISTS!', username, password)
            return jsonify(message='Username already exists, please choose a different username'), 409
          
        query = "INSERT INTO users (username, password_hash) VALUES (%s, %s)"
        # Hash the password before storing it
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        cursor.execute(query, (username, hashed_password))
        connection.commit()
        cursor.close()

        return jsonify(message='User registered successfully'), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/login', methods=['POST'])
def login():
    app.logger.info('Login button clicked')
    try:
        # get the JSON data from the request, and then extract the 'username' and 'password' fields.
        data = request.get_json()
        username = data['username']
        password = data['password']
        if password == "test1":
            hashed_password = password
        else:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        app.logger.info('U: %s, P: %s, HASH %s',username, password, hashed_password)

        # create a new cursor object, which is used to execute SQL commands, and define a SQL query
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username = %s"
        # execute the query
        cursor.execute(query, (username,))
        result = cursor.fetchall()
        app.logger.info('Response from DB: %s', result)
        cursor.close()

        # If user not found, db returns empty tuple
        if not result:
            return jsonify(message='User not found'), 404

        # test1 is not hashed
        if result[0][2] == "test1":
            if password == hashed_password:
                return jsonify(message='Login successful for test1'), 200
            else:
                return jsonify(message='Wrong password for test1'), 401
        # Check if the hashed password matches the one in the database
        elif bcrypt.checkpw(password.encode('utf-8'), result[0][2].encode('utf-8')):
            return jsonify(message='Login successful'), 200
        else:
            return jsonify(message='Wrong password'), 401
    except Exception as e:
        return jsonify(error=str(e)), 500
    
# TEST BUTTON ROUTE    
@app.route('/test', methods=['POST'])
def test():
    return jsonify(message='Test route called successfully'), 200

# LEAVE THIS AT THE BOTTOM!!
# Start the Flask application 
if __name__ == '__main__': #check in Python is used to determine whether the script is being run directly or it's being imported as a module.
    app.run(host='0.0.0.0', port=5000, debug=True)
