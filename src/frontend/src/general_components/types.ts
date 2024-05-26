
// src/types.ts

export interface Coordinates {
    lat: number;
    lng: number;
  }

export interface Location {
    id: number;
    coordinates: Coordinates;
    tel_num: string;
  }
  
  export interface LocationResponse {
    my_location : Location;
    plough_locations: Location[];
    waypoints: Location[];
    error?: string;
  }