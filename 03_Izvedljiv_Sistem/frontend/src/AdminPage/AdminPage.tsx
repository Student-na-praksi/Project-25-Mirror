
import { useState } from "react";

import AdminSideBand from "./AdminSideBand";
import { MenuBurgerButton } from "@/general_components/MenuBurgerButton";
import "./AdminPage-style.css";


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
          <AdminSideBand />
        </div>
        }

        <button style={{border: 0, padding: 0}} onClick={toggleBandPresent} ><MenuBurgerButton className="menu-burger" /></button>
      </div>
    </>
  )
}

export default AdminPage




