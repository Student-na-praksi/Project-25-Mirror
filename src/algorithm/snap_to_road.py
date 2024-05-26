



import pickle


import geopandas as gpd


from pyproj import Proj, Transformer
from shapely.geometry import LineString, Point




class SnapToRoad:

    def __init__(self):

        # Deserialize (unpickle) the objects
        with open('data.pkl', 'rb') as f:
            roads_gdf, remaining_intersection_gdf, remaining_intersections_line_ix_lists, _ = pickle.load(f)

        self.roads_gdf = roads_gdf
        self.remaining_intersection_gdf = remaining_intersection_gdf
        self.remaining_intersections_line_ix_lists = remaining_intersections_line_ix_lists


    # returns [closest_road_ix_1, closest_road_ix_2, ...]
    def snap_many_gps_to_road(self, gps_list):
        snapped_list = []
        for lon, lat in gps_list:
            snapped_list.append(self.snap_gps_to_road(lon, lat))
        return snapped_list




    def snap_gps_to_road(self, lon, lat):
        x, y = self.project_from_gps_to_slovene_system(lon, lat)
        return self.snap_to_road(x, y)


    # When working with geographic coordinates,
    # the convention is to use longitude (x) and latitude (y)
    
    def snap_to_road(self, lon, lat):
        # Find the closest road
        min_dist = float('inf')
        closest_road_ix = None
        for idx, geom in self.roads_gdf['geometry'].items():
            dist = geom.distance(Point(lon, lat))
            if dist < min_dist:
                min_dist = dist
                closest_road_ix = idx

        # # Find the closest intersection
        # min_dist = float('inf')
        # closest_intersection_ix = None
        # for idx, geom in self.remaining_intersection_gdf['geometry'].items():
        #     dist = geom.distance(Point(lon, lat))
        #     if dist < min_dist:
        #         min_dist = dist
        #         closest_intersection_ix = idx

        # # Find the closest road to the intersection
        # min_dist = float('inf')
        # closest_road_to_intersection = None
        # for road_idx in self.remaining_intersections_line_ix_lists[closest_intersection]:
        #     dist = self.roads_gdf.iloc[[road_idx]]['geometry'].values[0].distance(self.remaining_intersection_gdf.iloc[[closest_intersection]]['geometry'].values[0])
        #     if dist < min_dist:
        #         min_dist = dist
        #         closest_road_to_intersection = road_idx

        # return self.roads_gdf.iloc[[closest_road]]['geometry'].values[0].xy, self.roads_gdf.iloc[[closest_road_to_intersection]]['geometry'].values[0].xy

        return closest_road_ix #, closest_intersection_ix


    def project_from_gps_to_slovene_system(self, geometry_x, geometry_y):
        # I gave Pluzenje_Zelenice.prj to gpt4 and it gave me this proj string:
        # Define the projection using the PROJ string from the .prj file
        proj_string = """
            +proj=tmerc +lat_0=0 +lon_0=15 +k=0.9999 +x_0=500000 +y_0=-5000000
            +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs
        """

        out_proj = Proj(proj_string)
        in_proj = Proj(proj='latlong', datum='WGS84')

        transformer = Transformer.from_proj(in_proj, out_proj, always_xy=True)

        x, y = geometry_x, geometry_y
        x, y = transformer.transform(x, y)

        return x, y
    

    def project_from_slovene_to_gps_system(self, geometry_x, geometry_y):
        # I gave Pluzenje_Zelenice.prj to gpt4 and it gave me this proj string:
        # Define the projection using the PROJ string from the .prj file
        proj_string = """
            +proj=tmerc +lat_0=0 +lon_0=15 +k=0.9999 +x_0=500000 +y_0=-5000000
            +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs
        """

        in_proj = Proj(proj_string)
        out_proj = Proj(proj='latlong', datum='WGS84')

        transformer = Transformer.from_proj(in_proj, out_proj, always_xy=True)

        x, y = geometry_x, geometry_y
        x, y = transformer.transform(x, y)

        return x, y
    
    def gps_to_snapped_gps(self, lon, lat):
        x, y = self.project_from_gps_to_slovene_system(lon, lat)
        snapped_road_ix = self.snap_to_road(x, y)
        snapped_road = self.roads_gdf.iloc[[snapped_road_ix]]['geometry']

        curr_pos = Point(x, y)
        snapped_pos = snapped_road.project(curr_pos)
        closest_point = snapped_road.interpolate(snapped_pos)

        snapped_x, snapped_y = (closest_point.x, closest_point.y)
        snapped_lon, snapped_lat = self.project_from_slovene_to_gps_system(snapped_x, snapped_y)
        return snapped_lon, snapped_lat
