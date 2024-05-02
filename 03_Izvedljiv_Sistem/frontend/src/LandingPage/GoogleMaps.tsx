


// https://www.youtube.com/watch?v=PfZ4oLftItk

"use client";

import { useEffect, useState } from "react";
import {
  APIProvider,
  Map,
  AdvancedMarker,
  Pin,
  InfoWindow,
} from "@vis.gl/react-google-maps";

import {GeoJsonLayer} from '@deck.gl/layers';
import {DeckGlOverlay} from './deckgl-overlay';

const DATA_URL =
  'https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/bart.geo.json';

import type {Feature, GeoJSON} from 'geojson';


function GoogleMaps() {

  // const position = { lat: 53.54, lng: 10 };
  const position = {lat: 37.74, lng: -122.4}
  const [open, setOpen] = useState(false);
  
  console.log(import.meta.env.VITE_PUBLIC_GOOGLE_MAPS_API_KEY)
  console.log(import.meta.env.VITE_PUBLIC_MAP_ID)



  const [data, setData] = useState<GeoJSON | null>(null);

  useEffect(() => {
    fetch(DATA_URL)
      .then(res => res.json())
      .then(data => setData(data as GeoJSON));
  }, []);

  // console.log(process.env.PUBLIC_GOOGLE_MAPS_API_KEY)
  return (
    <APIProvider apiKey={import.meta.env.VITE_PUBLIC_GOOGLE_MAPS_API_KEY} >
      <div className="zemljevid">
        <Map 
          defaultZoom={9}
          defaultCenter={position}
          mapId={import.meta.env.VITE_PUBLIC_MAP_ID}>

          <DeckGlOverlay layers={getDeckGlLayers(data)} />

          <AdvancedMarker position={position} onClick={() => setOpen(true)}>
            <Pin
              background={"grey"}
              borderColor={"green"}
              glyphColor={"purple"}
            />
          </AdvancedMarker>

          {open && (
            <InfoWindow position={position} onCloseClick={() => setOpen(false)}>
              <p>I'm in Hamburg</p>
            </InfoWindow>
          )}

          {/* Tole rabimo: https://visgl.github.io/react-google-maps/examples/deckgl-overlay */}
          {/* https://visgl.github.io/react-google-maps/examples/directions */}



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
