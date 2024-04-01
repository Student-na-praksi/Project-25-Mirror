import geopandas as gpd


# automatically reads the associated files
# (.dbf, .prj, .shx, etc.) along with the .shp file:
gdf = gpd.read_file('pluzenje_MOC/Pluzenje_Zelenice.shp')




# # File path pattern using wildcard to match multiple shapefiles
# file_pattern = 'pluzenje_MOC/*.shp'

# # Read all shapefiles matching the pattern into a single GeoDataFrame
# merged_gdf = gpd.read_file(file_pattern)

# gdf = merged_gdf



# import pandas as pd

# # List of file paths to shapefiles
# shapefile_paths = ['path_to_shapefile1.shp', 'path_to_shapefile2.shp', 'path_to_shapefile3.shp']

# # Read each shapefile into a separate GeoDataFrame
# gdfs = [gpd.read_file(shp) for shp in shapefile_paths]

# # Concatenate GeoDataFrames into a single GeoDataFrame
# merged_gdf = pd.concat(gdfs, ignore_index=True)







print(gdf.head())

# Access geometry column
geometry = gdf.geometry
print(geometry)

# Access specific attribute columns
attribute_column = gdf['atr4']

import matplotlib.pyplot as plt

gdf.plot()
plt.show()
