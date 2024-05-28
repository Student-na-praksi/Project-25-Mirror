


// https://www.youtube.com/watch?v=PfZ4oLftItk

"use client";

// import { useEffect, useState } from "react";
import {
  APIProvider,
  Map
} from "@vis.gl/react-google-maps";

import {GeoJsonLayer} from '@deck.gl/layers';
import {DeckGlOverlay} from './deckgl-overlay';


import { useState, useEffect } from 'react';
import { fetchPloughLocationsAndWaypoints } from './api';
import { Location  } from './types';


// const DATA_URL =
//   'https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/bart.geo.json';

import type {Feature, GeoJSON} from 'geojson';

import roadsData from './roads.json';

import MyLocation from "./MyLocation";
import RouteMarker from "./RouteMarker";
import Plug from "./Plug";

import { FeatureCollection } from 'geojson';



let fake_ploughs: Location[] = []
for (let i = 0; i < 10; i++) {
  let ix = Math.floor(Math.random() * roadsData.features.length);

  let pos_array = roadsData.features[ix]?.geometry?.coordinates[0];
  
 let real_pos = { lat: pos_array?.[1] ?? 46.2398, lng: pos_array?.[0] ?? 15.2677 };

  let curr_plug = {id: i, coordinates: real_pos, tel_num: ("0" + (31123456 + i) + "")  };
  fake_ploughs.push(curr_plug);
}

 let fake_waypoints: Location[] = []
let init_ix = Math.floor(Math.random() * roadsData.features.length);
for (let i = 0; i < 5; i++) { 
  let pos_array = roadsData.features[init_ix+i]?.geometry?.coordinates[0];
  if (pos_array) {
    let real_pos = { lat: pos_array[1], lng: pos_array[0] };
    let curr_waipoint = {id: i, coordinates: real_pos, tel_num: ""};
    fake_waypoints.push(curr_waipoint);
  }
}







function GoogleMaps() {

  // const [my_location, setMyLocation] = useState<google.maps.LatLngLiteral | null>(null);
  // const [my_location, setMyLocation] = useState<Location>({});
  
  const celje_pos = { lat: 46.2398, lng: 15.2677};

  const my_loc: Location = {
    id: 0,
    coordinates: {
      lat: 46.24,
      lng: 15.26
    },
    tel_num: ""
  };


  // used for fetching custom location from algo_server
  // Meant for artificial locations.
  const [my_location, setMyLocation] = useState<Location>(my_loc);
  const [plough_locations, setPloughLocations] = useState<Location[] | []>(fake_ploughs);
  const [waypoints, setWaypoints] = useState<Location[] | []>(fake_waypoints);
  //const [setError] = useState<string | null>(null);
  const [id] = useState<number>(0);

  useEffect(() => {
    const getLocation = async () => {
      try {
        const data = await fetchPloughLocationsAndWaypoints(id);
        if (data.error) {
          setError(data.error);
          setMyLocation(my_loc);
          setPloughLocations(fake_ploughs);
          setWaypoints(fake_waypoints);
        } else {
          setMyLocation(data.my_location);
          setPloughLocations(data.plough_locations);
          setWaypoints(data.waypoints);
          setError("");
        }
      } catch (err) {
        if (err instanceof Error) {
          setError(err.message);
        } else {
          setError('An unknown error occurred');
        }
        setMyLocation(my_loc);
        setPloughLocations(fake_ploughs);
        setWaypoints(fake_waypoints);
      }
    };

    // Fetch data immediately and then every 300 milliseconds
    getLocation();
    // const intervalId = setInterval(getLocation, 100);

    // // Clear the interval on component unmount
    // return () => clearInterval(intervalId);
  }, [id]); // Add id as a dependency. The effect will run every time the id changes, and not on every render.


  const roadsData: FeatureCollection = {
    type: 'FeatureCollection',
    features: [],
  };

  return (
    <APIProvider apiKey={import.meta.env.VITE_PUBLIC_GOOGLE_MAPS_API_KEY} >
      <div className="zemljevid">
        <Map 
          defaultZoom={13}
          defaultCenter={celje_pos}
          mapId={import.meta.env.VITE_PUBLIC_MAP_ID}
          gestureHandling={'greedy'}>

          

          <DeckGlOverlay layers={getDeckGlLayers(roadsData)} />

          <MyLocation loc={my_location.coordinates}/>

          {plough_locations.map((item, index) => (
              <Plug key={index} position={item.coordinates} tel_num={item.tel_num} />
          ))}

          {waypoints.map((item, index) => (
              <RouteMarker key={index} position={item.coordinates} num_in_row={index+1} />
          ))}


          {/* <RouteMarker position={celje_pos} num_in_row={1} /> */}
          {/* <Plug position={some_plug_pos} tel_num={"031 123 456"} /> */}



        </Map>
      </div>
    </APIProvider>
  );
};

export default GoogleMaps;




function getDeckGlLayers(data: GeoJSON | null) {
  if (!data) return [];

  return [
    new GeoJsonLayer({
      id: 'geojson-layer',
      data,
      stroked: false,
      filled: true,
      extruded: true,
      pointType: 'circle',
      lineWidthScale: 20,
      lineWidthMinPixels: 4,
      getFillColor: [160, 160, 180, 200],
      getLineColor: (f: Feature) => {
        const hex = f?.properties?.color;

        if (!hex) return [0, 0, 0];

        return hex.match(/[0-9a-f]{2}/g)!.map((x: string) => parseInt(x, 16));
      },
      getPointRadius: 200,
      getLineWidth: 1,
      getElevation: 30
    })
  ];
}

function setError(message: string) {
  throw new Error("Err msg: " + message + "!");
}

