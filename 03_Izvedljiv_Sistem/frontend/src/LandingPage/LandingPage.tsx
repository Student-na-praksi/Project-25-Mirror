
import { useState } from "react";

import { AdminSideBand } from "./AdminSideBand";
import { MenuBurgerButton } from "./MenuBurgerButton";
import "./LandingPage-style.css";
import zemljevid from "@/assets/Zemljevid.png";

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
          <AdminSideBand />
        </div>
        }

        <button style={{border: 0, padding: 0}} onClick={toggleBandPresent} ><MenuBurgerButton className="menu-burger" /></button>
      </div>
    </>
  )
}

export default LandingPage




