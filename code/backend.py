from flask import Flask, request, jsonify, render_template

import mysql.connector
import bcrypt

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='kurir',
    password='kurir',
    database='tpo24'
)

# Create a Flask application
app = Flask(__name__)

# Configure the Flask application
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Handle the register endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    # Insert the user into the database
    cursor = connection.cursor()
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"

    # Hash a password for the first time, with a randomly-generated salt
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    # Check that a unhashed password matches one that has previously been hashed
    if bcrypt.checkpw(password, hashed):
        cursor.execute(query, (username, password))
        connection.commit()
        cursor.close()
        return jsonify(message='User registered successfully')
    else :
        return jsonify(message='Password does not match')


# Handle the button click endpoint
@app.route('/button-click', methods=['POST'])
def button_click():
    # Perform the desired action when the button is clicked
    # For example, update a value in the database or trigger some other functionality

    return jsonify(message='Button clicked successfully')

# Handle the index page
@app.route('/')
def index():
    return render_template('index.html')

# Start the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# Handle the register endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    # Insert the user into the database
    cursor = connection.cursor()
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"

    # Hash a password for the first time, with a randomly-generated salt
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    # Check that a unhashed password matches one that has previously been hashed
    if bcrypt.checkpw(password, hashed):
        cursor.execute(query, (username, password))
        connection.commit()
        cursor.close()
        return jsonify(message='User registered successfully')
    else :
        return jsonify(message='Password does not match')


# Handle the button click endpoint
@app.route('/button-click', methods=['POST'])
def button_click():
    # Perform the desired action when the button is clicked
    # For example, update a value in the database or trigger some other functionality

    return jsonify(message='Button clicked successfully')

# Start the Flask application
if __name__ == '__main__': #check in Python is used to determine whether the script is being run directly or it's being imported as a module.
    app.run(host='0.0.0.0', port=5000, debug=True)