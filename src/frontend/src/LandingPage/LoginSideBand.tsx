import "./LoginSideBand-style.css";
import { useState } from 'react';

function LoginSideBand() {

    const [name, setName] = useState('');
    const [pass, setPass] = useState('');



    const handleSubmit = () => {
        alert("Prijava v obravnavi.");
    }

    return (
        <div className="band">

            
            <div className="frame-2">
                <div className="rectangle">Prijavni podatki:</div>
                <div className="zahtevki">




                    <form onSubmit={handleSubmit}>
                        <br/>
                        <label htmlFor="name">Username:</label><br/>
                        <input type="text" id="name" name="name" value={name} onChange={(e) => setName(e.target.value)}/>
                        <br/><br/>
                        <label htmlFor="pass">Password:</label><br/>
                        <input type="text" id="pass" name="pass" value={pass} onChange={(e) => setPass(e.target.value)}/>
                        <br/><br/>
                        
                        <input className="zahtevek" type="submit" value="Log in"></input>
                    </form>
                
                </div>
            </div>
            
        </div>
    );
};

export default LoginSideBand;