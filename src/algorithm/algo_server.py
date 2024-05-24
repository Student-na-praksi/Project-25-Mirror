from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

# Create a new Flask web server from the Flask class
app = Flask(__name__, static_url_path='/static')
CORS(app) # This line enables CORS support on the Flask app. This allows the frontend to make requests to the backend.
# app will log all the messages which are at the level INFO or above.
app.logger.setLevel(logging.INFO)

# This line sets the configuration for the Flask application to pretty-print JSON output. This makes JSON output easier to read.
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True



















import json
import random

# Load the JSON data from a file
with open('vizualizacija/roads.json') as f:
    roads_data = json.load(f)

# Define the data structures
fake_ploughs = []
fake_waypoints = []

# Generate fake ploughs
for i in range(10):
    ix = random.randint(0, len(roads_data['features']) - 1)
    pos_array = roads_data['features'][ix]['geometry']['coordinates'][0]
    real_pos = {'lat': pos_array[1], 'lng': pos_array[0]}
    curr_plough = {'id': i, 'coordinates': real_pos, 'tel_num': f"0{31123456 + i}"}
    fake_ploughs.append(curr_plough)

# Generate fake waypoints
init_ix = random.randint(0, len(roads_data['features']) - 6)  # Ensure there are enough features
for i in range(5):
    pos_array = roads_data['features'][init_ix + i]['geometry']['coordinates'][0]
    real_pos = {'lat': pos_array[1], 'lng': pos_array[0]}
    curr_waypoint = {'id': i, 'coordinates': real_pos, 'tel_num': ""}
    fake_waypoints.append(curr_waypoint)

# Print the results (optional)
print("Fake Ploughs:")
for plough in fake_ploughs:
    print(plough)

print("\nFake Waypoints:")
for waypoint in fake_waypoints:
    print(waypoint)



























id = 0
my_loc = fake_ploughs[0]
del fake_ploughs[0]




@app.route('/get-locations', methods=['GET'])
def get_location():
    requested_id = request.args.get('id', type=int)
    
    if requested_id is None:
        return jsonify({"error": "Missing 'id' parameter"}), 400
    








    
    # location = next((loc for loc in locations if loc["id"] == location_id), None)
    location_response = {
        "my_location": my_loc,
        "plough_locations": fake_ploughs,
        "waypoints": fake_waypoints
    } 

    if location_response is None:
        return jsonify({"error": "Location not found"}), 404
    
    return jsonify(location_response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)
    