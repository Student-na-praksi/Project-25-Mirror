






import { useState } from "react";
import {
  AdvancedMarker,
  Pin,
  InfoWindow,
} from "@vis.gl/react-google-maps";

import snowplowIcon from "@/assets/snowplow.png";




let my_location: google.maps.LatLngLiteral | null = null;

if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(my_location_success, my_location_error);
} else {
  console.log("Geolocation not supported");
}

function my_location_success(position: any) {
  const latitude = position.coords.latitude;
  const longitude = position.coords.longitude;
  my_location = { lat: latitude, lng: longitude };
  console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);
}

function my_location_error() {
  console.log("Unable to retrieve your location");
}



function MyLocation() {
    const [open, setOpen] = useState(false);

    return(
        <>
            <AdvancedMarker position={my_location} onClick={() => setOpen(true)}>
                <Pin
                background={"red"}
                borderColor={"blue"}
                glyphColor={"purple"}
                />
            </AdvancedMarker>


            <AdvancedMarker position={my_location} onClick={() => setOpen(true)}>
                <img src={snowplowIcon} alt="snowplow" style={{ width: "50px" }}/>
            </AdvancedMarker>

            {open && (
            <InfoWindow position={my_location} onCloseClick={() => setOpen(false)}>
              <p>This pin represents you.</p>
            </InfoWindow>
          )}
        </>
    );
}

export default MyLocation;