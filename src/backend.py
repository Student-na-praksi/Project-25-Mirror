from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime
import mysql.connector
import bcrypt
import logging


# singelton design pattern
class DatabaseConnector:
    def __init__(self):
        # Create a connection to the MySQL database
        #self.connection = True
        self.connection = mysql.connector.connect(
           host='localhost',
           user='kurir',
           password='kurir',
           database='tpo25'
        )

    def connect(self):
        return self.connection

db_connector = DatabaseConnector()
connection = None

# Command pattern
class DatabaseHelper:
    def queryExec(self, connection, query_type, args):
        cursor = connection.cursor()
        if query_type == 'login':
            query = "SELECT * FROM users WHERE username = %s"
            cursor.execute(query, (args['username'],))
        elif query_type == 'register':
            query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(query, (args['username'], args['password']))
        elif query_type == 'addplow':
            query = """
            INSERT INTO plows (plowusername, baza, plastlat, plastlong, plasttime, online, `desc`) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (args['plowusername'], args['baza'], args['plastlat'], args['plastlong'], args['plasttime'], args['online'], args['desc']))
            connection.commit()
            cursor.close()
            return None
        else:
            raise ValueError('Invalid query type')
        result = cursor.fetchall()
        cursor.close()
        return result

db_helper = DatabaseHelper()

# Create a new Flask web server from the Flask class
app = Flask(__name__, static_url_path='/static')
CORS(app) # This line enables CORS support on the Flask app. This allows the frontend to make requests to the backend.
# app will log all the messages which are at the level INFO or above.
app.logger.setLevel(logging.INFO)

# This line sets the configuration for the Flask application to pretty-print JSON output. This makes JSON output easier to read.
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    
# Handle the index page
@app.route('/')
def renderHtml():
    return render_template('loginRegister.html')
  
# Log every incoming request
# @app.before_request
# def log_request():
#     app.logger.info('Request received: %s %s', request.method, request.path)

# Handle the register endpoint
@app.route('/register', methods=['POST'])
def register():
    app.logger.info('Register button clicked')
    global connection
    
    try:
        # If the connection to the database is not established try establishing a new connection
        if connection is None:
            try:
                connection = db_connector.connect()
            except Exception as e:
                return jsonify(message='The database is unreachable'), 500 # + str(e)
             
        # get the JSON data from the request, and then extract the 'username', 'password', and 'accountType' fields.
        data = request.get_json()
        username = data['username']
        password = data['password']
        telphone = data['telephone_number']
        accountType = data['type']
        app.logger.info('Inserting user: %s with password: %s and account type: %s into DB', username, password, telphone, accountType)
        
        #if(db_conn.writeUserToDb(username, password, telphone, accountType)):
        #    return jsonify(message='User registered successfully'), 200
        #else:
        # create a new cursor object, which is used to execute SQL commands, and define a SQL query
        cursor = connection.cursor()
        # Check if the username already exists in the database
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchall()
        if result:
            app.logger.info('User %s ALREADY EXISTS!', username, password)
            return jsonify(message='Username already exists, please choose a different username'), 409
          
        query = "INSERT INTO users (username, password_hash, acc_type) VALUES (%s, %s, %s)"
        # Hash the password before storing it
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        cursor.execute(query, (username, hashed_password, accountType))
        connection.commit()
        cursor.close()

        return jsonify(message='User registered successfully'), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/login', methods=['POST'])
def login():
    app.logger.info('Login button clicked')
    global connection

    try:
            
        # get the JSON data from the request, and then extract the 'username' and 'password' fields.
        data = request.get_json()
        username = data['username']
        password = data['password']
        # test1 is checked logaly
        if username == "test1":
            if password == "test1":
                return jsonify(message='Login successful for test1'), 200
            else:
                return jsonify(message='Wrong password for test1'), 401
        else:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        app.logger.info('U: %s, P: %s, HASH %s',username, password, hashed_password)

        # If the connection to the database is not established try establishing a new connection
        if connection is None:
            try:
                connection = db_connector.connect()
            except Exception as e:
                return jsonify(message='The database is unreachable'), 500 # + str(e)
            
        # create a new cursor object, which is used to execute SQL commands, and define a SQL query
        # cursor = connection.cursor()
        # query = "SELECT * FROM users WHERE username = %s"
        # # execute the query
        # cursor.execute(query, (username,))
        # result = cursor.fetchall()
        # app.logger.info('Response from DB: %s', result)
        # cursor.close()
        result = db_helper.queryExec(connection, 'login', {'username': username})

        # If user not found, db returns empty tuple
        if not result:
            return jsonify(message='User not found'), 404

        # Check if the hashed password matches the one in the database
        if bcrypt.checkpw(password.encode('utf-8'), result[0][2].encode('utf-8')):
            return jsonify(message='Login successful'), 200
        else:
            return jsonify(message='Wrong password'), 401
    except Exception as e:
        return jsonify(error=str(e)), 500
    
@app.route('/addplow', methods=['POST'])
def add_plow():
    # Get the data from the request
    #data = request.get_json()

    # # Check if all necessary data is provided
    # if 'plowusername' not in data or 'baza' not in data or 'plastlat' not in data or 'plastlong' not in data or 'plasttime' not in data or 'online' not in data or 'desc' not in data:
    #     return jsonify({'error': 'Missing data'}), 400

    global connection

    if connection is None:
        try:
            connection = db_connector.connect()
        except Exception as e:
            return jsonify(message='The database is unreachable'), 500 # + str(e)
        
    # Prepare the arguments for the query
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
    args = {
        'plowusername': "test1",
        'baza': "VOC",
        'plastlat': "46.17040",
        'plastlong': "14.31384",
        'plasttime': timestamp,
        'online': 1,
        'desc': "opisni opis"
    }
    # args = {
    #     'plowusername': data['plowusername'],
    #     'baza': data['baza'],
    #     'plastlat': data['plastlat'],
    #     'plastlong': data['plastlong'],
    #     'plasttime': data['plasttime'],
    #     'online': data['online'],
    #     'desc': data['desc']
    # }

    # Execute the query
    try:
        db_helper.queryExec(connection, 'addplow', args)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    # Return a success message
    return jsonify({'message': 'Plow added successfully'}), 200

# TEST BUTTON ROUTE    
@app.route('/test', methods=['POST'])
def test():
    return jsonify(message='Test route called successfully'), 200

@app.route('/activate_plow', methods=['POST'])
def activate_plow():
    # Validate the user is a manager?
    # Validate the target username is a plo¸w
    # Send the message to the plow 
    # After the ack, inform the client
    return jsonify(message='Plow is yes'), 200

@app.route('/deactivate_plow', methods=['POST'])
def deactivate_plow():
    # Validate the user is a manager?
    # Validate the target username is a plow
    # Send the message to the plow 
    # After the ack, inform the client
    return jsonify(message='Plow is no'), 200

@app.route('/get_plow_location', methods=['POST'])
def get_plow_location():
    # Validate the target username is a plow
    # Return plow's location to the client
    return jsonify(message='Plow is no'), 200

@app.route('/select_a_request', methods=['POST'])
def select_a_request():
    # Set a request as in progress and the plow
    # Notify the plow
    return jsonify(message='Plow is no'), 200

@app.route('/submit_a_request', methods=['POST'])
def submit_a_request():
    # Create a new request to clear the road location
    # Notify the client
    return jsonify(message='Plow is no'), 200

@app.route('/complete_a_request', methods=['POST'])
def complete_a_request():
    # Mark a request as completed for the client/plow
    # Notify the client
    return jsonify(message='Plow is no'), 200

@app.route('/get_roads', methods=['GET'])
def get_roads():
    # Return the roads and the state
    return jsonify(message='Plow is no'), 200

@app.route('/get_plows', methods=['GET'])
def get_plows():
    # Get all the plows from DB and return all active ones
    return jsonify(message='Plow is no'), 200

@app.route('/get_next_requests', methods=['GET'])
def get_next_requests():
    # Validate the client is a plow or manager
    # Return the next <n> requests for a plow
    return jsonify(message='Plow is no'), 200

@app.route('/get_requests', methods=['GET'])
def get_requests():
    # Validate the client is a plow or manager
    # Return all available requests
    return jsonify(message='Plow is no'), 200

@app.route('/get_free_plows', methods=['GET'])
def get_free_plows():
    #TODO

    # Validate the user is a manager?
    # Get from DB users who are plows
    # Get their location
    # Send the message to the client
    return jsonify(message='Plow is no'), 200

# LEAVE THIS AT THE BOTTOM!!
# Start the Flask application 
if __name__ == '__main__': #check in Python is used to determine whether the script is being run directly or it's being imported as a module.
    app.run(host='0.0.0.0', port=5000, debug=True)