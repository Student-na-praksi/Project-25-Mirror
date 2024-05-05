
import { useState } from "react";

import LoginSideBand from "./LoginSideBand";
import { LoginButton } from "@/general_components/LoginButton";
import "./LandingPage-style.css";


import GoogleMaps from "@/general_components/GoogleMaps";


function AdminPage() {

  const [bandPresent, setBandPresent] = useState(false);

  const toggleBandPresent = () => {
    setBandPresent(!bandPresent);
  };
  
  return (
    <>
      <div className="desktop">
        <div className="zemljevid">
          <GoogleMaps />
        </div>

        {bandPresent && 
        <div className="main-band"> 
          <LoginSideBand />
        </div>
        }

        <button style={{border: 0, padding: 0}} onClick={toggleBandPresent} ><LoginButton className="menu-burger" /></button>
      </div>
    </>
  )
}

export default AdminPage




