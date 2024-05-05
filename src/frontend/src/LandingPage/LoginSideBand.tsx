import "./LoginSideBand-style.css";
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function LoginSideBand() {

    const [name, setName] = useState('');
    const [pass, setPass] = useState('');

    const navigate = useNavigate();



    const handleSubmit = () => {
        navigate('/admin');
        alert("Prijava uspešna.");
    }

    return (
        <div className="band">

            
            <div className="frame-2">
                <div className="rectangle">Prijavni podatki:</div>
                <div className="zahtevki">




                    <form onSubmit={handleSubmit}>
                        <br/>
                        <label htmlFor="name">Uporabniško ime:</label><br/>
                        <input type="text" id="name" name="name" value={name} onChange={(e) => setName(e.target.value)}/>
                        <br/><br/>
                        <label htmlFor="pass">Geslo:</label><br/>
                        <input type="text" id="pass" name="pass" value={pass} onChange={(e) => setPass(e.target.value)}/>
                        <br/><br/>
                        
                        <input className="zahtevek" type="submit" value="Prijava"></input>
                    </form>
                
                </div>
            </div>
            
        </div>
    );
};

export default LoginSideBand;