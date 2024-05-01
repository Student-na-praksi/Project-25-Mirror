
import { useState } from "react";

import { Band } from "./Band";
import { Frame } from "./Frame";
import "./desktop-style.css";
import zemljevid from "./assets/Zemljevid.png";

function LandingPage() {

  const [bandPresent, setBandPresent] = useState(false);

  const toggleBandPresent = () => {
    setBandPresent(!bandPresent);
  };
  

  return (
    <>
      <div className="desktop">
        <img className="zemljevid" alt="Zemljevid" src={zemljevid} />
        {bandPresent && 
        <div className="main-band">
          <Band />
        </div>
        }
        <button style={{border: 0, padding: 0}} onClick={toggleBandPresent} ><Frame className="frame-3" /></button>
      </div>
    </>
  )
}

export default LandingPage




