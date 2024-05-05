import "./UserSideBand-style.css";
import { useState } from 'react';

function LoginSideBand() {

    const [address, setAddress] = useState('');
    const [size, setSize] = useState('');



    const handleSubmit = () => {
        alert("Prijava v obravnavi.");
    }

    return (
        <div className="band">

            
            <div className="frame-2">
                <div className="rectangle">Oddaj zahtevek za pluženje:</div>
                <div className="zahtevki">




                    <form onSubmit={handleSubmit}>
                        <br/>
                        <label htmlFor="address">Naslov:</label><br/>
                        <input type="text" id="address" name="address" value={address} onChange={(e) => setAddress(e.target.value)}/>
                        <br/><br/>
                        <label htmlFor="size">Plužna površina v kvadratnih metrih:</label><br/>
                        <input type="text" id="size" name="size" value={size} onChange={(e) => setSize(e.target.value)}/>
                        <br/><br/>
                        
                        <input className="zahtevek" type="submit" value="Oddaj"></input>
                    </form>
                
                </div>
            </div>
            
        </div>
    );
};

export default LoginSideBand;