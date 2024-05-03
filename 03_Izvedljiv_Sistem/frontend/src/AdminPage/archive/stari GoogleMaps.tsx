


// https://www.youtube.com/watch?v=PfZ4oLftItk

"use client";

import { useState } from "react";
import {
  APIProvider,
  Map,
  AdvancedMarker,
  Pin,
  InfoWindow,
} from "@vis.gl/react-google-maps";


function GoogleMaps() {

  const position = { lat: 53.54, lng: 10 };
  const [open, setOpen] = useState(false);
  
  console.log(import.meta.env.VITE_PUBLIC_GOOGLE_MAPS_API_KEY)
  console.log(import.meta.env.VITE_PUBLIC_MAP_ID)
  // console.log(process.env.PUBLIC_GOOGLE_MAPS_API_KEY)
  return (
    <APIProvider apiKey={import.meta.env.VITE_PUBLIC_GOOGLE_MAPS_API_KEY} >
      <div className="zemljevid">
        <Map zoom={9} center={position} mapId={import.meta.env.VITE_PUBLIC_MAP_ID}>
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



// Copied from npm package: @react-google-maps/api page

// import React from 'react'
// import { GoogleMap, useJsApiLoader } from '@react-google-maps/api';

// const containerStyle = {
//   width: '400px',
//   height: '400px'
// };

// const center = {
//   lat: -3.745,
//   lng: -38.523
// };

// function Maps() {
//   const { isLoaded } = useJsApiLoader({
//     id: 'google-map-script',
//     googleMapsApiKey: "YOUR_API_KEY"
//   })

//   const [map, setMap] = React.useState(null)

//   const onLoad = React.useCallback(function callback(map: any) {
//     // This is just an example of getting and using the map instance!!! don't just blindly copy!
//     const bounds = new window.google.maps.LatLngBounds(center);
//     map.fitBounds(bounds);

//     setMap(map)
//   }, [])

//   const onUnmount = React.useCallback(function callback(map: any) {
//     setMap(null)
//   }, [])

//   return isLoaded ? (
//       <GoogleMap
//         mapContainerStyle={containerStyle}
//         center={center}
//         zoom={10}
//         onLoad={onLoad}
//         onUnmount={onUnmount}
//       >
//         { /* Child components, such as markers, info windows, etc. */ }
//         <></>
//       </GoogleMap>
//   ) : <></>
// }

// export default Maps