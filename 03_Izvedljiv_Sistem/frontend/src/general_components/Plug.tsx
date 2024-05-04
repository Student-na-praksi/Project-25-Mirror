
import { useState } from "react";
import {
  AdvancedMarker,
  Pin,
  InfoWindow,
} from "@vis.gl/react-google-maps";

import snowplowIcon from "@/assets/snowplow.png";





interface PlugProps {
    position: {
      lat: number;
      lng: number;
    };
    tel_num: string;
}


function Plug({ position, tel_num }: PlugProps) {

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
                <img src={snowplowIcon} alt="snowplow" style={{ width: "50px" }}/>
        </AdvancedMarker>

        {open && (
            <InfoWindow position={position} onCloseClick={() => setOpen(false)}>
            <p>Their telephone number: {tel_num}</p>
            </InfoWindow>
        )}

    </>

    );
}

export default Plug;