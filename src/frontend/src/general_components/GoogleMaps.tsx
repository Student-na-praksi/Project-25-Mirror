


// https://www.youtube.com/watch?v=PfZ4oLftItk

"use client";

// import { useEffect, useState } from "react";
import {
  APIProvider,
  Map
} from "@vis.gl/react-google-maps";

import {GeoJsonLayer} from '@deck.gl/layers';
import {DeckGlOverlay} from './deckgl-overlay';


// const DATA_URL =
//   'https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/bart.geo.json';

import type {Feature, GeoJSON} from 'geojson';

import roadsData from './roads.json';

import MyLocation from "./MyLocation";
import RouteMarker from "./RouteMarker";
import Plug from "./Plug";

import { FeatureCollection, Geometry, GeoJsonProperties } from 'geojson';





let plugi: any[] = []
for (let i = 0; i < 10; i++) {
  let ix = Math.floor(Math.random() * (roadsData?.features?.length || 0));

  let pos_array = roadsData?.features?.[ix]?.geometry?.coordinates?.[0];
  let real_pos = { lat: pos_array?.[1], lng: pos_array?.[0] };
  plugi.push({pos: real_pos, tel_num: ("0" + (31123456 + i) + "")  });
}

let waypoints: any[] = []
let init_ix = Math.floor(Math.random() * (roadsData?.features?.length || 0));
for (let i = 0; i < 5; i++) { 
  let pos_array = roadsData?.features?.[init_ix+i]?.geometry?.coordinates?.[0];
  let real_pos = { lat: pos_array?.[1], lng: pos_array?.[0] };
  waypoints.push(real_pos);
}







function GoogleMaps() {

  // const [my_location, setMyLocation] = useState<google.maps.LatLngLiteral | null>(null);
  // const [my_location, setMyLocation] = useState<Location>({});
  
  const celje_pos = { lat: 46.2398, lng: 15.2677};



  const roadsData: FeatureCollection<Geometry, GeoJsonProperties> = require('./roads.json');


  return (
    <APIProvider apiKey={import.meta.env.VITE_PUBLIC_GOOGLE_MAPS_API_KEY} >
      <div className="zemljevid">
        <Map 
          defaultZoom={13}
          defaultCenter={celje_pos}
          mapId={import.meta.env.VITE_PUBLIC_MAP_ID}
          gestureHandling={'greedy'}>


          <DeckGlOverlay layers={getDeckGlLayers(roadsData)} />

          <MyLocation />

          {plugi.map((item, index) => (
              <Plug key={index} position={item.pos} tel_num={item.tel_num} />
          ))}

          {waypoints.map((item, index) => (
              <RouteMarker key={index} position={item} num_in_row={index+1} />
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

