from flask import Flask, request, jsonify

import mysql.connector

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_database_name'
)

# Create a Flask application
app = Flask(__name__)

# Configure the Flask application
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

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
    cursor.execute(query, (username, password))
    connection.commit()
    cursor.close()

    return jsonify(message='User registered successfully')

# Handle the button click endpoint
@app.route('/button-click', methods=['POST'])
def button_click():
    # Perform the desired action when the button is clicked
    # For example, update a value in the database or trigger some other functionality

    return jsonify(message='Button clicked successfully')

# Start the Flask application
if __name__ == '__main__':
    app.run(port=3000)