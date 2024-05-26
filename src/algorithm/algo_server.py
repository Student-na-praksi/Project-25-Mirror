from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

# Create a new Flask web server from the Flask class
app = Flask(__name__, static_url_path='/static')
CORS(app) # This line enables CORS support on the Flask app. This allows the frontend to make requests to the backend.
# app will log all the messages which are at the level INFO or above.

app.logger.setLevel(logging.INFO)
# app.logger.setLevel(logging.ERROR)
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)

# This line sets the configuration for the Flask application to pretty-print JSON output. This makes JSON output easier to read.
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

















from graph_maker import Graph


import json
import random

import threading
import time

class Positions(threading.Thread):

    def __init__(self):
        
        threading.Thread.__init__(self)
        self.running = True

        # Load the JSON data from a file
        with open('vizualizacija/roads.json') as f:
            roads_data = json.load(f)

        # Define the data structures
        self.fake_ploughs = []
        # self.fake_waypoints = []

        # Generate fake ploughs
        for i in range(10):
            # ix = random.randint(0, len(roads_data['features']) - 1)
            ix = i * 100
            pos_array = roads_data['features'][ix]['geometry']['coordinates'][0]
            real_pos = {'lat': pos_array[1], 'lng': pos_array[0]}
            curr_plough = {'id': i, 'coordinates': real_pos, 'tel_num': f"0{31123456 + i}"}
            self.fake_ploughs.append(curr_plough)

        # # Generate fake waypoints
        # init_ix = random.randint(0, len(roads_data['features']) - 6)  # Ensure there are enough features
        # for i in range(5):
        #     pos_array = roads_data['features'][init_ix + i]['geometry']['coordinates'][0]
        #     real_pos = {'lat': pos_array[1], 'lng': pos_array[0]}
        #     curr_waypoint = {'id': i, 'coordinates': real_pos, 'tel_num': ""}
        #     self.fake_waypoints.append(curr_waypoint)

        # # Print the results (optional)
        # print("Fake Ploughs:")
        # for plough in fake_ploughs:
        #     print(plough)

        # print("\nFake Waypoints:")
        # for waypoint in fake_waypoints:
        #     print(waypoint)



        self.id = 0 # same as saying ix in the fake_ploughs
        self.my_loc = self.fake_ploughs[self.id]['coordinates']



        self.graph = Graph()
        
        self.severities = [ix/self.graph.num_of_roads for ix in range(0, self.graph.num_of_roads)]
        self.graph.set_connection_severities(self.severities)
        self.graph.node_severities_from_roads()
        
        self.graph.set_plugi([(plough['coordinates']['lng'], plough['coordinates']['lat']) for plough in self.fake_ploughs])

        self.graph.perform_severity_passing_steps(10)

        self.graph.make_plugi_waypoints()
        self.fake_waypoints = self.graph.get_plugi_waypoints_gps_coords()

        self.printout_ix = 0



    def reset_plugi(self):
        # self.graph = Graph()
        
        self.graph.set_plugi([(plough['coordinates']['lng'], plough['coordinates']['lat']) for plough in self.fake_ploughs])

        # print("Here 1")
        # self.graph.set_connection_severities(severities)
        # self.graph.node_severities_from_roads()
        # self.graph.perform_severity_passing_steps(10)

        self.graph.make_plugi_waypoints(delete_first_waypoint=True)
        # print("Here 2")
        
        self.fake_waypoints = self.graph.get_plugi_waypoints_gps_coords()
        # print("Here 3")
        # print("self.fake_waypoints")
        # print(self.fake_waypoints)
    
    def get_waypoints(self):
        my_waypoints = self.fake_waypoints[self.id]
        correct_format = [{"lng": waypoint[0], "lat": waypoint[1]} for waypoint in my_waypoints]
        return correct_format


    
    def run(self):
        while self.running:

            for ix in range(len(self.fake_ploughs)):
                # print("self.fake_ploughs[self.id]['coordinates']['lng'], self.fake_ploughs[self.id]['coordinates']['lat'], self.fake_waypoints[self.id][0][0], self.fake_waypoints[self.id][0][1]")
                # print(self.fake_ploughs[self.id]['coordinates']['lng'], self.fake_ploughs[self.id]['coordinates']['lat'], self.fake_waypoints[self.id][0][0], self.fake_waypoints[self.id][0][1])
                try:
                    curr_lng, curr_lat = self.fake_ploughs[ix]['coordinates']['lng'], self.fake_ploughs[ix]['coordinates']['lat']
                    if type(curr_lng) == list:
                        curr_lng = curr_lng[0]
                    if type(curr_lat) == list:
                        curr_lat = curr_lat[0]

                    if isinstance(curr_lng, np.ndarray):
                        curr_lng = curr_lng[0]
                    if isinstance(curr_lat, np.ndarray):
                        curr_lat = curr_lat[0]

                    x_dif = self.fake_waypoints[ix][0][0] - curr_lng
                    y_dif = self.fake_waypoints[ix][0][1] - curr_lat
                    
                    norm = (x_dif**2 + y_dif**2)**0.5
                except:
                    print("ix")
                    print(ix)
                    print("curr_lng")
                    print(curr_lng)
                    print("self.fake_waypoints")
                    print(self.fake_waypoints)
                    
                

                try:
                    if type(norm) == list:
                        norm = norm[0]
                    if isinstance(norm, np.ndarray):
                        norm = norm[0]

                    if norm < 0.00001:

                        norm = 1
                        self.reset_plugi()
                        continue

                    x_dif /= norm
                    y_dif /= norm
                except:
                    print("x_dif, y_dif, norm")
                    print(x_dif, y_dif, norm)
                    print("self.fake_ploughs[ix]['coordinates']['lng']")
                    print(self.fake_ploughs[ix]['coordinates']['lng'])
                    
                    # # cause it again:
                    # if norm < 0.1:
                    #     x_dif /= norm

                movement = 0.1

                if ix == 0:
                    print("curr_lng")
                    print(curr_lng)
                    print("curr_lng + movement * (x_dif)")
                    print(curr_lng + movement * (x_dif))
                    print("self.fake_ploughs[ix]['coordinates']['lng']")
                    print(self.fake_ploughs[ix]['coordinates']['lng'])
                    print("self.fake_waypoints[ix][0][0]")
                    print(self.fake_waypoints[ix][0][0])

                self.fake_ploughs[ix]['coordinates']['lng'] = curr_lng + movement * (x_dif)
                self.fake_ploughs[ix]['coordinates']['lat'] = curr_lat + movement * (y_dif)

                if ix == 0:
                    print("self.fake_ploughs[ix]['coordinates']['lng']")
                    print(self.fake_ploughs[ix]['coordinates']['lng'])
            
                # plough['coordinates']['lat'] += random.uniform(-0.0001, 0.0001) # 0.01 # random.uniform(-0.0001, 0.01001)
                # plough['coordinates']['lng'] += random.uniform(-0.0001, 0.0001) # 0.01 #random.uniform(-0.0001, 0.0001)
            # print("Thread is running")
            time.sleep(0.01)

            self.my_loc = self.fake_ploughs[self.id]['coordinates']



            # print("self.fake_ploughs[0]")
            # print(self.fake_ploughs[0])
            # print("self.fake_waypoints[0]")
            # print(self.fake_waypoints[0])

            if self.printout_ix % 100 == 0:

                print("self.fake_ploughs[0]")
                print(self.fake_ploughs[0])
                print("self.fake_waypoints[0]")
                print(self.fake_waypoints[0])

                # print("self.fake_ploughs[self.id]['coordinates']['lng'], self.fake_ploughs[self.id]['coordinates']['lat'], self.fake_waypoints[self.id][0][0], self.fake_waypoints[self.id][0][1]")
                # print(self.fake_ploughs[self.id]['coordinates']['lng'], self.fake_ploughs[self.id]['coordinates']['lat'], self.fake_waypoints[self.id][0][0], self.fake_waypoints[self.id][0][1])
                # print("self.fake_ploughs[self.id]['coordinates']['lng'], self.fake_ploughs[self.id]['coordinates']['lat'], self.my_loc")
                # print(self.fake_ploughs[self.id]['coordinates']['lng'], self.fake_ploughs[self.id]['coordinates']['lat'], self.my_loc)
                # print("")

            self.printout_ix += 1

            

    
    def stop(self):
        self.running = False


















import numpy as np

def convert_numpy_to_list(d):
    for key, value in d.items():
        if isinstance(value, dict):
            convert_numpy_to_list(value)
        elif isinstance(value, np.ndarray):
            d[key] = value.tolist()
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    convert_numpy_to_list(item)



positions = Positions()





@app.route('/get-locations', methods=['GET'])
def get_location():
    requested_id = request.args.get('id', type=int)
    
    if requested_id is None:
        return jsonify({"error": "Missing 'id' parameter"}), 400
    








    
    # location = next((loc for loc in locations if loc["id"] == location_id), None)
    location_response = {
        "my_location": positions.my_loc,
        "plough_locations": positions.fake_ploughs,
        "waypoints": positions.get_waypoints()
    } 

    if location_response is None:
        return jsonify({"error": "Location not found"}), 404
    
    try:
        returner = jsonify(convert_numpy_to_list(location_response))
    except:
        returner = jsonify({"error": "Could not jsonify the response"})
        print("location_response")
        print(location_response)

    return returner

if __name__ == '__main__':
    positions.start()

    try:
        app.run(host='0.0.0.0', port=7000, debug=True)
    finally:
        positions.stop()
        positions.join()