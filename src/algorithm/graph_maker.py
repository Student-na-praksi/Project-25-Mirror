import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt


ZMANJSAJ_OBSEG = False
SHUFFLE = False




# Možni paths
shapefile_paths = ['pluzenje_MOC/Pluzenje_Zelenice.shp', "pluzenje_MOC/Pluzenje_intervencijske_poti_brvi.shp", 'pluzenje_MOC/Pluzenje_parkirisca.shp', 'pluzenje_MOC/Pluzenje_VOC.shp']

# Trenutno beremo le zelenice - lahko bi gledali tudi ostale.
roads_gdf = gpd.read_file('pluzenje_MOC/Pluzenje_Zelenice.shp')


# Razreže roads_gdf po teh koordinatah [xmin:xmax, ymin:ymax]
# Tako sem zmanjšal obseg za namen testiranja.
if ZMANJSAJ_OBSEG:
    roads_gdf = roads_gdf.cx[518750:520250,122800:124400]














"""
Izris črt, kjer ima vsaka svojo barvo - glede na row index v roads_gdf-ju.
Shufflanje vrstic v roads_gdf-ju, ker so bližnje ceste v podatkih sosednje vrstice,
in so potem istih barv in se ne vidi segmentacija med njimi in se nič ne vidi.
Kot seed se konstantno uporablja 50, da je lažje debuggat.
"""

if SHUFFLE:
    shuffled_roads_gdf = roads_gdf.sample(frac=1, random_state=50)
    roads_gdf = shuffled_roads_gdf

roads_gdf = roads_gdf.reset_index(drop=True)

rgba_road_colors = [plt.cm.viridis(idx/len(roads_gdf)) for idx in range(0, len(roads_gdf))]








"""
Tu se zgodi, da najdemo presečišča med cestami.
Podatki so v osnovi tako podani, da je posamezna cesta en LineString,
ki gre od enega križišča do naslednega. Tako da podatki so že dobri - ni nič treba lomit cest.
Kar pa je treba naredit, je najti njihova presečišča - pač na koncih se sekajo.

S pomočjo roads_gdf.sindex lahko efektivno omejimo iskanje kandidatov za presečišče.

Ker se bo zgodilo, da bi prvi bil intersection z drugim, in drugi s prvim (bi bilo podvajanje)
bomo omejili kandidate na le te, ki imajo višji index od trenutnega kandidata.

S pomočjo: if intersection.geom_type == 'Point':   preprečimo primere, ko je neka cesta podvojena
in je zato overlayed čez sebe in je presečišče med tema kopijama LineString, in ne Point.

intersection_gdf je gdf točk (Point), ki so intersections.
intersections_line_ix_pairs je list parov cest.
i-ti element vsebuje list z 2 številoma - to sta idx pripadajočih cest iz roads_gdf.

Problem je sedaj, da pač neko trojno križišče ima potem tri intersectione - vsak par teh treh cest je svoj intersection.
To je potem treba združiti - kar pa naredimo spodaj.
"""

# Create a spatial index for the GeoDataFrame
sindex = roads_gdf.sindex

# Initialize an empty list to store intersecting geometries
intersections_line_ix_pairs = []
intersection_geometries = []

# Iterate over pairs of geometries
for i, geom1 in roads_gdf['geometry'].items():
    # Get the bounding box of the current geometry
    bbox = geom1.bounds
    # Get the indices of candidate geometries that intersect with the bounding box
    candidates = list(sindex.intersection(bbox))

    candidates = [j for j in candidates if j > i]

    # Check intersection with candidate geometries
    for j in candidates:
        geom2 = roads_gdf.iloc[j]['geometry']
        if i != j and geom1.intersects(geom2):
            # If the geometries intersect, add them to the list of intersections
            
            intersection = geom1.intersection(geom2)

            # Izkaze se, da so doloceni line-i podvojeni, in potem nastane celoten line intersectiona.
            if intersection.geom_type == 'Point':
                intersections_line_ix_pairs.append((i, j))
                intersection_geometries.append(intersection)


# Print the list of intersections
# print("Intersections:", intersections_line_ix_pairs)


# Create a GeoSeries from the list of intersection geometries
intersection_series = gpd.GeoSeries(intersection_geometries)

# Create a GeoDataFrame from the GeoSeries
intersection_gdf = gpd.GeoDataFrame(geometry=intersection_series, crs=roads_gdf.crs)

# Reset the index of the GeoDataFrame
intersection_gdf = intersection_gdf.reset_index(drop=True)

# Print the GeoDataFrame
# print(intersection_gdf)










"""
Tu se sedaj te iz intersections_line_ix_pairs združijo.
Nastane remaining_intersections_line_ix_lists
in nastane remaining_intersection_gdf.

Spet istoležna elementa sta povezana:
i-ti list iz remaining_intersections_line_ix_lists vsebuje ceste, ki se sekajo v
i-tem intersectionu v remaining_intersection_gdf.
"""


# !!!!!!!!!!!!!!
# Eliminating replications of the same intersection.
# For example, three-way intersections have a problem - they need to have the intersections merged into one.

# Create a spatial index for the GeoDataFrame
sindex = intersection_gdf.sindex

# Every intersection ix has its' list of intersection ixs, which are extremely close to it.
# The list only contains ixs higher than the own ix.
# Later we will simply go from 0 to the last index and merge the list of sames - but only for the ixs that
# haven't undergone a merging already.
interIx2listOfSames = dict()

for i in range(0, len(intersection_gdf)):
    interIx2listOfSames[i] = []

buffer_distance = 0.03

# Iterate over pairs of geometries
for ix, point in intersection_gdf["geometry"].items():
    # Get the bounding box of the current geometry
    
    bbox = point.buffer(buffer_distance).bounds

    # Get the indices of candidate geometries that intersect with the bounding box
    candidates = list(sindex.intersection(bbox))

    candidates = [j for j in candidates if j > ix]

    interIx2listOfSames[ix].extend(candidates)





def merge(ixs_of_inters, line_data):
    lines_present = set()

    for ix in ixs_of_inters:
        lines_present.update(line_data[ix])
    
    return list(lines_present)



remaining_intersection_geometries = []
remaining_intersections_line_ix_lists = []

already_merged = [False for i in range(0, len(intersection_gdf))]

for i in range(0, len(intersection_gdf)):
    
    if already_merged[i]:
        continue

    to_merge = interIx2listOfSames[i]
    to_merge.append(i)

    for ix in to_merge:
        already_merged[ix] = True


    remaining_intersection_geometries.append(intersection_geometries[i])

    lines_present = merge(to_merge, intersections_line_ix_pairs)
    remaining_intersections_line_ix_lists.append(lines_present)



remaining_intersection_series = gpd.GeoSeries(remaining_intersection_geometries)

remaining_intersection_gdf = gpd.GeoDataFrame(geometry=remaining_intersection_series, crs=roads_gdf.crs)


# print("remaining_intersections_line_ix_lists with more than two elements:")
# print([i for i in remaining_intersections_line_ix_lists if len(i) > 2])













""" Now let's make the lines and points into a GeoJSON file. """


# Drop all of the properties except for geometry
roads_gdf = roads_gdf[["geometry"]]






# We don't need the transformation to GPS.
# In fact, we need length of roads and it's wrong after the transformation.

"""
# Transform these coordinates to the GPS coordinates

from pyproj import Proj, Transformer
from shapely.geometry import LineString, Point

# I gave Pluzenje_Zelenice.prj to gpt4 and it gave me this proj string:
# Define the projection using the PROJ string from the .prj file
proj_string = """ """
    +proj=tmerc +lat_0=0 +lon_0=15 +k=0.9999 +x_0=500000 +y_0=-5000000
    +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs
"""
"""
in_proj = Proj(proj_string)
out_proj = Proj(proj='latlong', datum='WGS84')

transformer = Transformer.from_proj(in_proj, out_proj, always_xy=True)

def transform_geometry(geometry, transformer):
    if geometry.geom_type == 'LineString':
        transformed_points = [transformer.transform(x, y) for x, y in geometry.coords]
        return LineString(transformed_points)
    elif geometry.geom_type == 'Point':
        x, y = geometry.x, geometry.y
        x, y = transformer.transform(x, y)
        return Point(x, y)
    
    else:
        return None

# Apply the transformation to each geometry
roads_gdf['geometry'] = roads_gdf['geometry'].apply(transform_geometry, transformer=transformer)

# CRS Not Transformed: Setting the CRS using set_crs does not transform the geometries to the new CRS; it only assigns the CRS to the GeoDataFrame. 
# If you need to transform the geometries to match the new CRS, you should use the to_crs method instead.
roads_gdf.set_crs('epsg:4326', inplace=True, allow_override=True)




def rgba_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


# This line makes it so that there are only 7 colours. Trying to make things easier for the browser.
rgba_road_colors = [plt.cm.viridis( (idx % 7) * (1/6)) for idx in range(0, len(roads_gdf))]

hex_code_road_colors = [rgba_to_hex(int(rgba[0]*255), int(rgba[1]*255), int(rgba[2]*255)) for rgba in rgba_road_colors]

# add the hex color property
roads_gdf["color"] = hex_code_road_colors
roads_gdf.to_file("roads.json", driver='GeoJSON')


# Apply the transform to intersections
remaining_intersection_gdf['geometry'] = remaining_intersection_gdf['geometry'].apply(transform_geometry, transformer=transformer)
"""








import numpy as np


# print("roads_gdf:")
# print(roads_gdf)

# print("remaining_intersection_gdf:")
# print(remaining_intersection_gdf)
# print("remaining_intersections_line_ix_lists:")
# print(remaining_intersections_line_ix_lists)










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











# reverse remaining_intersections_line_ix_lists so every road has its intersection ixs
lines_to_remaining_intersections_ix_lists = [[] for i in range(0, len(roads_gdf))]
for i, line_ix_list in enumerate(remaining_intersections_line_ix_lists):
    for line_ix in line_ix_list:
        lines_to_remaining_intersections_ix_lists[line_ix].append(i)






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











from matplotlib.colors import LinearSegmentedColormap, Normalize

import numpy as np
from multiprocessing import Pool

class Connection:
    
        def __init__(self, line_ix, roads_gdf, lines_to_remaining_intersections_ix_lists):
                        
            self.road_idx = line_ix

            self.intersections = lines_to_remaining_intersections_ix_lists[line_ix]

            self.length = roads_gdf.iloc[[line_ix]].geometry.length
            self.severity = 1

        def set_severity(self, severity):
            self.severity = severity
    


def set_severity_helper(args):
    connection, severity = args
    connection.set_severity(severity)
    return connection


def node_severities_helper(args):

    # list_of_connection_tuples are all (ix, conn_obj) for the
    # current intersection
    list_of_connection_tuples, node_severities = args

    severity = 0

    for pair_inter_ix, _ in list_of_connection_tuples:
        severity += node_severities[pair_inter_ix]
    return severity

class Graph:

    def __init__(self, roads_gdf, remaining_intersection_gdf, lines_to_remaining_intersections_ix_lists):
        
        self.num_of_intersections = len(remaining_intersection_gdf)
        self.num_of_roads = len(roads_gdf)

        self.connections = np.empty(self.num_of_roads, dtype=object)
        self.intersection_to_connections = np.empty(self.num_of_intersections, dtype=object)

        self.node_severities = np.zeros(self.num_of_intersections)
        self.next_node_severities = np.zeros(self.num_of_intersections)


        for road_ix in range(0, self.num_of_roads):

            # Create the connection
            self.connections[road_ix] = Connection(road_ix, roads_gdf, lines_to_remaining_intersections_ix_lists)


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




    def set_connection_severities(self, severities):

        for road_ix in range(0, self.num_of_roads):
            self.connections[road_ix].set_severity(severities[road_ix])


        # # Create a list of (connection, severity) tuples
        # args = zip(self.connections, severities)

        # # Use multiprocessing Pool to parallelize the task
        # with Pool() as pool:
        #     self.connections = np.array(pool.map(set_severity_helper, args))
        
    
    def normalize_node_severities(self):

        self.node_severities = np.clip(self.node_severities, 0, 1)

        mean = np.mean(self.node_severities)
        # make the new mean 0.5
        self.node_severities =  (self.node_severities / mean) * 0.5

        self.node_severities = np.clip(self.node_severities, 0, 1)



        # max_severity = np.max(self.node_severities)
        # min_severity = np.min(self.node_severities)

        # divisor = (max_severity - min_severity)
        # self.node_severities = (self.node_severities - min_severity) / divisor if divisor != 0 else (self.node_severities - min_severity)


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
                node_severity = self.connections[road_ix].severity * self.connections[road_ix].length
                self.next_node_severities[intersection_ix] += node_severity
        
        
        # To nisem testiral pa pomoje ni treba. To se itak redko izvaja.
        """def node_severities_from_roads_helper(args):
            connection, node_severities = args
            for intersection_ix in connection.intersections:
                node_severity = connection.severity * connection.length
                node_severities[intersection_ix] += node_severity
            return node_severities
        
        # Create a list of (connection, node_severities) tuples
        args = zip(self.connections, [np.zeros(self.num_of_intersections) for i in range(0, self.num_of_roads)])

        # Use multiprocessing Pool to parallelize the task
        with Pool() as pool:
            self.next_node_severities = pool.map(node_severities_from_roads_helper, args)
        """


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
        




        # def node_severities_helper(args):

        #     # list_of_connection_tuples are all (ix, conn_obj) for the
        #     # current intersection
        #     list_of_connection_tuples, node_severities = args

        #     severity = 0

        #     for pair_inter_ix, _ in list_of_connection_tuples:
        #         severity += node_severities[pair_inter_ix]

        #     return severity


        # # This passes the reference to node_severities to all helper functions.
        # args = zip(self.intersection_to_connections, [self.node_severities for _ in range(len(self.intersection_to_connections))])

        # # Use multiprocessing Pool to parallelize the task
        # with Pool() as pool:
        #     self.next_node_severities = np.array(pool.map(node_severities_helper, args))



        self.update_node_severities()
    


    def plot(self):
        
        # Create a plot
        fig, ax = plt.subplots()

        # Reverse the 'RdYlGn' colormap to get a green-to-red transition
        green_to_red = plt.colormaps['RdYlGn_r']
        rgba_road_colors = [green_to_red(road.severity) for road in self.connections]
        # rgba_road_colors = [plt.cm.viridis(road.severity) for road in self.connections]

        roads_gdf['severity'] = [road.severity for road in self.connections]
        roads_gdf.plot(ax=ax, column='severity', cmap=green_to_red, linewidth=2)

        # for idx, geom in roads_gdf['geometry'].items():
        #     roads_gdf.iloc[[idx]].plot(ax=ax, color=rgba_road_colors[idx], linewidth=2)



        remaining_intersection_gdf['severity'] = self.node_severities
        # remaining_intersection_gdf['severity'] = [1 for i in range(0, len(remaining_intersection_gdf))]
        
        # remaining_intersection_gdf.plot(ax=ax, column='severity', cmap=green_to_red)
        
        # for idx, geom in remaining_intersection_gdf['geometry'].items():
        #     remaining_intersection_gdf.iloc[[idx]].plot(ax=ax, color=green_to_red(self.node_severities[idx]), markersize=30)

        

        # Create a normalization instance with mean at 0.5
        norm = Normalize(vmin=0, vmax=1)

        # Extract x and y coordinates
        x = remaining_intersection_gdf.geometry.x
        y = remaining_intersection_gdf.geometry.y

        # Plot the points with colors based on the 'severity' attribute
        sc = ax.scatter(x, y, c=remaining_intersection_gdf['severity'], cmap=green_to_red, s=30, norm=norm, edgecolors='black', linewidths=0.5) #, edgecolor='k')



        """
        # Plotanje list-a pripadajočih cest na vsak intersection.
        for idx, row in  remaining_intersection_gdf.iterrows():
            # Get the coordinates of the point to place the label
            x, y = row.geometry.x, row.geometry.y
            
            # Get the label corresponding to the current geometry
            label = remaining_intersections_line_ix_lists[idx]
            
            # Add the label to the plot
            ax.annotate(label, (x, y), xytext=(3, 3), textcoords="offset points")
        """


        plt.show()
                



PRINTOUT = False

graph = Graph(roads_gdf, remaining_intersection_gdf, lines_to_remaining_intersections_ix_lists)

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


for i in range(0, 1000):
    for j in range(0, 10):
        graph.node_severities_from_nodes()
    print("graph.node_severities")
    print(graph.node_severities)
    graph.plot()




























