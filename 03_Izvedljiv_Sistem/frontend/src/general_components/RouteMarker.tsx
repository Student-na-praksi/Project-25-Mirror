




import { useState } from "react";
import {
  AdvancedMarker,
  Pin,
  InfoWindow,
} from "@vis.gl/react-google-maps";



interface RouteMarkerProps {
    position: {
      lat: number;
      lng: number;
    };
    num_in_row: number;
}


function RouteMarker({ position, num_in_row }: RouteMarkerProps) {

    const [open, setOpen] = useState(false);

    return(
    <>
        <AdvancedMarker position={position} onClick={() => setOpen(true)}>
            <Pin
            background={"grey"}
            borderColor={"green"}
            glyphColor={"purple"}
            />
        </AdvancedMarker>

        <AdvancedMarker position={position} onClick={() => setOpen(true)}>
            <div style={{ width: "10px"}}><p style={{ fontSize: "15px", color: "white", textAlign: "center", backgroundColor: "purple" }}>{num_in_row}</p></div>
        </AdvancedMarker>

        {open && (
            <InfoWindow position={position} onCloseClick={() => setOpen(false)}>
            <p>This is your {num_in_row}. goal.</p>
            </InfoWindow>
        )}

    </>

    );
}

export default RouteMarker;