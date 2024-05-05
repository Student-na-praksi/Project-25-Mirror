from flask import Flask, request, jsonify, render_template
import database_connector as db_conn
import bcrypt
import logging


# Create a new Flask web server from the Flask class
app = Flask(__name__, static_url_path='/static')
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
        if(not db_conn.connectionEstablished):
            try:
                db_conn.connectToSQL()
                if(not db_conn.connectionEstablished):
                     return jsonify(message='The database is unreachable'), 500 # + str(e)
            except Exception as e:
                return jsonify(message='The database is unreachable'), 500 # + str(e)
             
        # get the JSON data from the request, and then extract the 'username', 'password', and 'accountType' fields.
        data = request.get_json()
        username = data['username']
        password = data['password']
        telphone = data['telephone_number']
        accountType = data['type']
        app.logger.info('Inserting user: %s with password: %s and account type: %s into DB', username, password, telphone, accountType)
        
        if(db_conn.writeUserToDb(username, password, telphone, accountType)):
            return jsonify(message='User registered successfully'), 200
        else:
            app.logger.info('User %s ALREADY EXISTS!', username, password)
            return jsonify(message='Username already exists, please choose a different username'), 409
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

        if(not db_conn.connectionEstablished):
            try:
                db_conn.connectToSQL()
                if(not db_conn.connectionEstablished):
                     return jsonify(message='The database is unreachable'), 500 # + str(e)
            except Exception as e:
                return jsonify(message='The database is unreachable'), 500 # + str(e)
        
        success, log, code = db_conn.validateLogin(username, password)
        app.logger.info('Response from DB: %s', log)
        
        if(code == 200):
            message = 'Login successful'
        elif(code == 401):
            message = 'Wrong password'
        elif(code == 404):
            message = 'User not found'

        return jsonify(message=message), code
    except Exception as e:
        return jsonify(error=str(e)), 500
    
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
