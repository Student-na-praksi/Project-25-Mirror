import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt


ZMANJSAJ_OBSEG = False




# Možni paths
shapefile_paths = ['pluzenje_MOC/Pluzenje_Zelenice.shp', "pluzenje_MOC/Pluzenje_intervencijske_poti_brvi.shp", 'pluzenje_MOC/Pluzenje_parkirisca.shp', 'pluzenje_MOC/Pluzenje_VOC.shp']

# Trenutno beremo le zelenice - lahko bi gledali tudi ostale.
roads_gdf = gpd.read_file('pluzenje_MOC/Pluzenje_Zelenice.shp')


# Razreže roads_gdf po teh koordinatah [xmin:xmax, ymin:ymax]
# Tako sem zmanjšal obseg za namen testiranja.
if ZMANJSAJ_OBSEG:
    roads_gdf = roads_gdf.cx[518750:520250,122800:124400]





# Prelged podatkov
if True:
    pd.set_option('display.max_columns', None)
    print(roads_gdf.head())
    roads_gdf.to_csv("Zelenice.csv", index=False)

    # Access geometry column
    geometry = roads_gdf.geometry
    print("Geometry here:")
    print(geometry)

    # Access specific attribute columns
    attribute_column = roads_gdf['atr4']

    roads_gdf.plot()
    plt.show()






# Create a plot
fig, ax = plt.subplots()





"""
Izris črt, kjer ima vsaka svojo barvo - glede na row index v roads_gdf-ju.
Shufflanje vrstic v roads_gdf-ju, ker so bližnje ceste v podatkih sosednje vrstice,
in so potem istih barv in se ne vidi segmentacija med njimi in se nič ne vidi.
Kot seed se konstantno uporablja 50, da je lažje debuggat.
"""

shuffled_roads_gdf = roads_gdf.sample(frac=1, random_state=50).reset_index(drop=True)
roads_gdf = shuffled_roads_gdf
rgba_road_colors = [plt.cm.viridis(idx/len(roads_gdf)) for idx in range(0, len(roads_gdf))]

# Iterate over each geometry and plot it with a different color
for idx, geom in roads_gdf['geometry'].items():
    roads_gdf.iloc[[idx]].plot(ax=ax, color=rgba_road_colors[idx], linewidth=2)
    # roads_gdf.iloc[[idx]].plot(ax=ax, color=plt.cm.viridis(idx/len(roads_gdf)), linewidth=2)

# Add title and labels
plt.title('Plot of LINESTRINGs with Different Colors')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# plt.show()

print("Sem premešal.")






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





# Kaksno sranje je, ce ne merge-aš ampak samo prikažeš intersectione:
if False:
    intersection_gdf.plot(ax=ax)

    # for idx, geom in intersection_gdf['geometry'].items():
    #     intersection_gdf.iloc[[idx]].plot(ax=ax, color=plt.cm.viridis(idx/len(intersection_gdf)), linewidth=2)

    for idx, row in  intersection_gdf.iterrows():
        # Get the coordinates of the point to place the label
        x, y = row.geometry.x, row.geometry.y
        
        # Get the label corresponding to the current geometry
        label = intersections_line_ix_pairs[idx]
        
        # Add the label to the plot
        ax.annotate(label, (x, y), xytext=(3, 3), textcoords="offset points")

    plt.show()









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


remaining_intersection_gdf.plot(ax=ax)

# print("remaining_intersections_line_ix_lists with more than two elements:")
# print([i for i in remaining_intersections_line_ix_lists if len(i) > 2])



# Plotanje list-a pripadajočih cest na vsak intersection.
for idx, row in  remaining_intersection_gdf.iterrows():
    # Get the coordinates of the point to place the label
    x, y = row.geometry.x, row.geometry.y
    
    # Get the label corresponding to the current geometry
    label = remaining_intersections_line_ix_lists[idx]
    
    # Add the label to the plot
    ax.annotate(label, (x, y), xytext=(3, 3), textcoords="offset points")


plt.show()











""" Now let's make the lines and points into a GeoJSON file. """


# Drop all of the properties except for geometry
roads_gdf = roads_gdf[["geometry"]]




# Transform these coordinates to the GPS coordinates

from pyproj import Proj, Transformer
from shapely.geometry import LineString

# I gave Pluzenje_Zelenice.prj to gpt4 and it gave me this proj string:
# Define the projection using the PROJ string from the .prj file
proj_string = """
    +proj=tmerc +lat_0=0 +lon_0=15 +k=0.9999 +x_0=500000 +y_0=-5000000
    +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs
"""
in_proj = Proj(proj_string)
out_proj = Proj(proj='latlong', datum='WGS84')

transformer = Transformer.from_proj(in_proj, out_proj, always_xy=True)

def transform_geometry(geometry, transformer):
    if geometry.geom_type == 'LineString':
        transformed_points = [transformer.transform(x, y) for x, y in geometry.coords]
        return LineString(transformed_points)
    
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





# remaining_intersection_gdf.to_file("intersections.geojson", driver='GeoJSON')










# import geopandas as gpd
# import networkx as nx

# # Assuming gdf is your GeoDataFrame with LINESTRING geometries

# # Create an empty graph
# G = nx.Graph()

# # Iterate over each pair of LINESTRINGs and check for intersections
# for i, line1 in gdf['geometry'].items():
#     for j, line2 in gdf['geometry'].items():
#         if i != j and line1.intersects(line2):
#             # Add an edge to the graph if the two lines intersect
#             G.add_edge(i, j)

# # Print the adjacency list of the graph
# print("Adjacency list of the graph:")
# print(dict(G.adjacency()))





















# from matplotlib.colors import Normalize
# from shapely.geometry import LineString, MultiLineString

# # Assuming gdf is your GeoDataFrame with a 'geometry' column containing LINESTRINGs

# # Function to split a LineString at its intersections and return the resulting segments
# def split_line_at_intersections(line, intersecting_geometries):
#     segments = [line]  # Start with the original LineString
#     for inter_line in intersecting_geometries:
#         new_segments = []
#         for segment in segments:
#             # Split the segment at the intersection with the current intersecting LineString
#             difference = segment.difference(inter_line)
#             if difference.is_empty:  # No difference, keep the original segment
#                 new_segments.append(segment)
#             elif isinstance(difference, MultiLineString):  # Multiple resulting geometries
#                 new_segments.extend(difference.geoms)
#             else:  # Single resulting geometry
#                 new_segments.append(difference)
#         segments = new_segments
#     return segments



# # Assuming gdf is your GeoDataFrame with a 'geometry' column containing LINESTRINGs

# # Create a spatial index for the GeoDataFrame
# sindex = gdf.sindex

# non_intersected_gdf = gpd.GeoDataFrame(geometry=[], crs=gdf.crs)


# # Iterate over each LINESTRING, split it at intersections, and plot each resulting segment with a different color
# for idx, geom in gdf['geometry'].items():
#     line = geom
#     intersecting_indices = list(sindex.intersection(line.bounds))
#     intersecting_geometries = gdf.iloc[intersecting_indices]['geometry'].tolist()
#     segments = split_line_at_intersections(line, intersecting_geometries)
#     new_rows = gpd.GeoDataFrame(geometry=segments, crs=gdf.crs)
#     # non_intersected_gdf = non_intersected_gdf.append(new_rows, ignore_index=True)
    
#     non_intersected_gdf = pd.concat([non_intersected_gdf, new_rows], ignore_index=True)



# shuffled_gdf = non_intersected_gdf.sample(frac=1).reset_index(drop=True)
# gdf = shuffled_gdf




# # Create a plot
# fig, ax = plt.subplots()

# # Iterate over each geometry and plot it with a different color
# for idx, geom in gdf['geometry'].items():
#     gdf.iloc[[idx]].plot(ax=ax, color=plt.cm.viridis(idx/len(gdf)), linewidth=2)

# # Add title and labels
# plt.title('Plot of LINESTRINGs with Different Colors')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# # Show the plot
# plt.show()



















