


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















function GoogleMaps() {

  // const position = { lat: 53.54, lng: 10 };
  // const [my_location, setMyLocation] = useState<google.maps.LatLngLiteral | null>(null);
  // const [my_location, setMyLocation] = useState<Location>({});
  // const position = {lat: 37.74, lng: -122.4}
  // const position = {lat: 46.253145591316489, lng: 15.24886631345186}
  const celje_pos = { lat: 46.2398, lng: 15.2677};

  const some_plug_pos = { lat: 46.2098, lng: 15.2877};




  // const [data, setData] = useState<GeoJSON | null>(null);

  // useEffect(() => {
  //   fetch(DATA_URL)
  //     .then(res => res.json())
  //     .then(data => setData(data as GeoJSON));
  // }, []);









  // console.log(process.env.PUBLIC_GOOGLE_MAPS_API_KEY)
  return (
    <APIProvider apiKey={import.meta.env.VITE_PUBLIC_GOOGLE_MAPS_API_KEY} >
      <div className="zemljevid">
        <Map 
          defaultZoom={13}
          defaultCenter={celje_pos}
          mapId={import.meta.env.VITE_PUBLIC_MAP_ID}
          gestureHandling={'greedy'}>

          <DeckGlOverlay layers={getDeckGlLayers(roadsData)} />

          {/* <Directions /> */}

          <MyLocation />

          <RouteMarker position={celje_pos} num_in_row={1} />

          <Plug position={some_plug_pos} tel_num={"031 123 456"} />




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



// function Directions() {

//   const breadcrumbs = [
//     { lat: 15.288974858778088, lng: 46.228298866878177 },
//     { lat: 15.264821959821901, lng: 46.228551616117961 },
//     { lat: 15.274667986171538, lng: 46.251323056553879 },
//     { lat: 15.283619307236656, lng: 46.25681642416037 },
//     { lat: 15.288974858778088, lng: 46.228298866878177}
//   ];



//   const map = useMap();
//   const routesLibrary = useMapsLibrary('routes');
//   const [directionsService, setDirectionsService] =
//     useState<google.maps.DirectionsService>();
//   const [directionsRenderer, setDirectionsRenderer] =
//     useState<google.maps.DirectionsRenderer>();
//   const [routes, setRoutes] = useState<google.maps.DirectionsRoute[]>([]);
//   const [routeIndex, setRouteIndex] = useState(0);
//   const selected = routes[routeIndex];
//   const leg = selected?.legs[0];

//   // Initialize directions service and renderer
//   useEffect(() => {
//     if (!routesLibrary || !map) return;
//     setDirectionsService(new routesLibrary.DirectionsService());
//     setDirectionsRenderer(new routesLibrary.DirectionsRenderer({map}));
//   }, [routesLibrary, map]);






//   // Use directions service
//   useEffect(() => {
//     if (!directionsService || !directionsRenderer) return;


//     const waypoints = breadcrumbs.slice(1, breadcrumbs.length - 1).map(location => ({
//       location: new google.maps.LatLng(location.lat, location.lng),
//       stopover: true
//     }));
  
//     const origin = breadcrumbs[0];
//     const destination = breadcrumbs[breadcrumbs.length - 1];


//     directionsService.route({
//       origin: new google.maps.LatLng(origin.lat, origin.lng),
//       destination: new google.maps.LatLng(destination.lat, destination.lng),
//       waypoints: waypoints,
//       travelMode: google.maps.TravelMode.WALKING,
//       // travelMode: google.maps.TravelMode.DRIVING,
//       provideRouteAlternatives: true
//     })
//     .then(response => {
//       directionsRenderer.setDirections(response);
//       setRoutes(response.routes);
//     });

//     // directionsService
//     //   .route({
//     //     origin: '100 Front St, Toronto ON',
//     //     destination: '500 College St, Toronto ON',
//     //     travelMode: google.maps.TravelMode.DRIVING,
//     //     provideRouteAlternatives: true
//     //   })
//     //   .then(response => {
//     //     directionsRenderer.setDirections(response);
//     //     setRoutes(response.routes);
//     //   });



//     return () => directionsRenderer.setMap(null);
//   }, [directionsService, directionsRenderer, breadcrumbs]);

//   // Update direction route
//   useEffect(() => {
//     if (!directionsRenderer) return;
//     directionsRenderer.setRouteIndex(routeIndex);
//   }, [routeIndex, directionsRenderer]);

//   if (!leg) return null;

//   return (
//     <div className="directions">
//       <h2>{selected.summary}</h2>
//       <p>
//         {leg.start_address.split(',')[0]} to {leg.end_address.split(',')[0]}
//       </p>
//       <p>Distance: {leg.distance?.text}</p>
//       <p>Duration: {leg.duration?.text}</p>

//       <h2>Other Routes</h2>
//       <ul>
//         {routes.map((route, index) => (
//           <li key={route.summary}>
//             <button onClick={() => setRouteIndex(index)}>
//               {route.summary}
//             </button>
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// }
