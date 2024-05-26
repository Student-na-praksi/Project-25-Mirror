





import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np


# print("roads_gdf:")
# print(roads_gdf)

# print("remaining_intersection_gdf:")
# print(remaining_intersection_gdf)
# print("remaining_intersections_line_ix_lists:")
# print(remaining_intersections_line_ix_lists)


from snap_to_road import SnapToRoad

import pickle






"""

# Create a plot
fig, ax = plt.subplots()


for idx, geom in roads_gdf['geometry'].items():
    roads_gdf.iloc[[idx]].plot(ax=ax, color=rgba_road_colors[idx], linewidth=2)


remaining_intersection_gdf.plot(ax=ax)



# Plotanje list-a pripadajočih cest na vsak intersection.
for idx, row in  remaining_intersection_gdf.iterrows():
    # Get the coordinates of the point to place the label
    x, y = row.geometry.x, row.geometry.y
    
    # Get the label corresponding to the current geometry
    label = remaining_intersections_line_ix_lists[idx]
    
    # Add the label to the plot
    ax.annotate(label, (x, y), xytext=(3, 3), textcoords="offset points")


plt.show()
"""




# Deserialize (unpickle) the objects
with open('data.pkl', 'rb') as f:
    roads_gdf, remaining_intersection_gdf, remaining_intersections_line_ix_lists, lines_to_remaining_intersections_ix_lists = pickle.load(f)












# # I guess these are the roads that are so small and close together, that they fall in the buffer_size thing.
# # They are nowhere to be found on the graph. Dunno. Just skip them.

# all_have_2 = all([len(i) <= 2 for i in lines_to_remaining_intersections_ix_lists])
# print("All lines have less than 2 intersections: ", all_have_2)

# temp_np = np.array(lines_to_remaining_intersections_ix_lists, dtype=object)
# truth_full_np = np.array([len(i) for i in lines_to_remaining_intersections_ix_lists])
# truth_full_np = truth_full_np > 2
# truth_np = np.where(truth_full_np)[0]
# # print(truth_np)
# # for idx in truth_np:
# #     print("lines_to_remaining_intersections_ix_lists[idx]:")
# #     print(lines_to_remaining_intersections_ix_lists[idx])


# fig, ax = plt.subplots()

# # Reverse the 'RdYlGn' colormap to get a green-to-red transition
# green_to_red = plt.cm.get_cmap('RdYlGn_r')
# rgba_road_colors = [green_to_red(1) if truth_full_np[ix] else green_to_red(1) for ix in range(0, len(roads_gdf))]
# # Iterate over each geometry and plot it with a different color

# for idx, geom in roads_gdf['geometry'].items():
#     roads_gdf.iloc[[idx]].plot(ax=ax, color=rgba_road_colors[idx], linewidth=2)

# # remaining_intersection_gdf['severity'] = self.node_severities
# remaining_intersection_gdf.plot(ax=ax) #, column='severity', cmap=green_to_red, markersize=30)


# plt.show()



class Plugi:

    def __init__(self):

        self.snap_to_road = SnapToRoad()
        self.plugi_gps_coord_tuples = []
        self.plugi_current_connection_ixs = []
        self.plugi_intersection_ixs = []
        self.length = 0

    
    def set_plugi(self, gps_coord_tuple_list):

        self.plugi_gps_coord_tuples = gps_coord_tuple_list

        self.length = len(gps_coord_tuple_list)

        self.plugi_current_connection_ixs = self.snap_to_road.snap_many_gps_to_road(gps_coord_tuple_list)

        self.plugi_intersection_ixs = [lines_to_remaining_intersections_ix_lists[ix] for ix in self.plugi_current_connection_ixs]
        





from matplotlib.colors import LinearSegmentedColormap, Normalize

import numpy as np
from multiprocessing import Pool

class Connection:
    
        def __init__(self, line_ix):
                        
            self.road_idx = line_ix

            self.intersections = lines_to_remaining_intersections_ix_lists[line_ix]

            self.length = roads_gdf.iloc[line_ix].geometry.length
            self.severity = 1

        def set_severity(self, severity):
            self.severity = severity
    



class Graph:

    def __init__(self): #, roads_gdf, remaining_intersection_gdf, lines_to_remaining_intersections_ix_lists):
        
        self.num_of_intersections = len(remaining_intersection_gdf)
        self.num_of_roads = len(roads_gdf)

        self.connections = np.empty(self.num_of_roads, dtype=object)
        self.intersection_to_connections = np.empty(self.num_of_intersections, dtype=object)

        self.node_severities = np.zeros(self.num_of_intersections)
        self.next_node_severities = np.zeros(self.num_of_intersections)

        self.plugi = Plugi()
        self.plugi_waypoints = []


        for road_ix in range(0, self.num_of_roads):

            # Create the connection
            self.connections[road_ix] = Connection(road_ix)


            # Add corresponding (pair_intersection_ix, connection_ix) to the 
            # involved intersections (max 2 should be involved, so this is a bit too general)
            # assert len(self.connections[road_ix].intersections) <= 2
            # In fact, this fails for a small number of roads.
            # But we just don't care because it's only a few.
            for intersection_ix in self.connections[road_ix].intersections:

                for pair_intersection_ix in self.connections[road_ix].intersections:
                    
                    if self.intersection_to_connections[intersection_ix] is None:
                        self.intersection_to_connections[intersection_ix] = []
                    
                    # skip if the intersection is yourself
                    if intersection_ix == pair_intersection_ix:
                        continue

                    self.intersection_to_connections[intersection_ix].append((pair_intersection_ix, road_ix))


    def set_plugi(self, gps_coord_tuple_list):
        self.plugi.set_plugi(gps_coord_tuple_list)
    
    def make_plugi_waypoints(self, delete_first_waypoint=False):

        new_waypoints = []

        for ix in range(0, self.plugi.length):

            curr_wps = []

            already_chosen_ixs = []

            try:
                neighbouring_intersections = self.plugi.plugi_intersection_ixs[ix]
                curr_ix = np.argsort([self.node_severities[ix] for ix in neighbouring_intersections])[0]
                curr_waypoint_ix = neighbouring_intersections[curr_ix] # direktno podani ix-i, torej brez [0]
                curr_wps.append(curr_waypoint_ix)
                already_chosen_ixs.append(curr_waypoint_ix)


                for i in range(2):
                    new_neighbours = self.intersection_to_connections[curr_waypoint_ix]
                    new_neighbours = [tup[0] for tup in new_neighbours if tup[0] not in already_chosen_ixs]
                    curr_ix = np.argsort([self.node_severities[ix] for ix in new_neighbours])[0] 
                    curr_waypoint_ix = neighbouring_intersections[curr_ix]
                    curr_wps.append(curr_waypoint_ix)
                    already_chosen_ixs.append(curr_ix)
                
                if delete_first_waypoint:
                    del curr_wps[0]

                new_waypoints.append(curr_wps)

            except:
                new_waypoints.append([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]) # some fake stuff that should get a plug to some 
                # road that has nodes, and then it works fine from there
                continue
        
        
        self.plugi_waypoints = new_waypoints


    def get_plugi_waypoints_gps_coords(self):
        returner = []
        for wps in self.plugi_waypoints:
            curr_wps = []
            for wp in wps:
                x, y = (remaining_intersection_gdf.iloc[wp].geometry.x, remaining_intersection_gdf.iloc[wp].geometry.y)
                x, y = self.plugi.snap_to_road.project_from_slovene_to_gps_system(x, y)
                curr_wps.append((x, y))
            returner.append(curr_wps)
        
        return returner
            


    def set_connection_severities(self, severities):

        for road_ix in range(0, self.num_of_roads):
            self.connections[road_ix].set_severity(severities[road_ix])

    
    def normalize_node_severities(self):

        self.node_severities = np.clip(self.node_severities, 0, 1)

        mean = np.mean(self.node_severities)
        # make the new mean 0.5
        self.node_severities =  (self.node_severities / mean) * 0.5

        self.node_severities = np.clip(self.node_severities, 0, 1)




    def update_node_severities(self):
        self.node_severities = self.next_node_severities
        self.next_node_severities = np.zeros(self.num_of_intersections)

        self.normalize_node_severities()


    # meant to initialize the severities
    def node_severities_from_roads(self):

        self.next_node_severities = np.zeros(self.num_of_intersections)

        for road_ix in range(0, self.num_of_roads):
            
            # There are only a few such roeads for some reason. We don't want them to mess up normalization.
            intersects = self.connections[road_ix].intersections
            if len(intersects) > 2:
                continue

            for intersection_ix in intersects:
                # print("self.connections[road_ix].severity")
                # print(self.connections[road_ix].severity)
                # print("self.connections[road_ix].length")
                # print(self.connections[road_ix].length)
                node_severity = self.connections[road_ix].severity * self.connections[road_ix].length
                # print("node_severity")
                # print(node_severity)
                self.next_node_severities[intersection_ix] += node_severity
        
        self.update_node_severities()
            


    def node_severities_from_nodes(self):



        for inter_ix in range(0, self.num_of_intersections):

            # This should never hold. Let us fail.
            # if self.intersection_to_connections[inter_ix] is None:
            #     continue
            

            node_severity = 0
            curr_conns = self.intersection_to_connections[inter_ix]

            for pair_inter_ix, _ in curr_conns:
                node_severity += self.node_severities[pair_inter_ix]

            self.next_node_severities[inter_ix] = node_severity
        



        self.update_node_severities()
    

    def perform_severity_passing_steps(self, num_steps=5):
        for _ in range(num_steps):
            self.node_severities_from_nodes()



    def plot(self):
        
        # Create a plot
        fig, ax = plt.subplots()

        # Reverse the 'RdYlGn' colormap to get a green-to-red transition
        green_to_red = plt.colormaps['RdYlGn_r']

        roads_gdf['severity'] = [road.severity for road in self.connections]
        roads_gdf.plot(ax=ax, column='severity', cmap=green_to_red, linewidth=2)




        remaining_intersection_gdf['severity'] = self.node_severities


        # Create a normalization instance with mean at 0.5
        norm = Normalize(vmin=0, vmax=1)

        # Extract x and y coordinates
        x = remaining_intersection_gdf.geometry.x
        y = remaining_intersection_gdf.geometry.y

        # Plot the points with colors based on the 'severity' attribute
        sc = ax.scatter(x, y, c=remaining_intersection_gdf['severity'], cmap=green_to_red, s=30, norm=norm, edgecolors='black', linewidths=0.5) #, edgecolor='k')


        plt.show()
    

                







if __name__ == "__main__":

    PRINTOUT = False
    graph = Graph()#roads_gdf, remaining_intersection_gdf, lines_to_remaining_intersections_ix_lists)


    severities = [ix/graph.num_of_roads for ix in range(0, graph.num_of_roads)]

    if PRINTOUT:
        print("severities")
        print(severities)

    graph.set_connection_severities(severities)

    if PRINTOUT:
        print("[conn.severity for conn in graph.connections]")
        print([conn.severity for conn in graph.connections])

    graph.node_severities_from_roads()
    print("graph.node_severities")
    print(graph.node_severities)
    graph.plot()

    # Serialize (pickle) the objects
    with open('graph.pkl', 'wb') as f:
        pickle.dump(graph, f)



    for i in range(0, 1000):
        for j in range(0, 10):
            graph.node_severities_from_nodes()
        print("graph.node_severities")
        print(graph.node_severities)
        graph.plot()




























