import "./AdminSideBand-style.css";

function AdminSideBand() {

    const zahtevki_test = ["Hiša 1", "Podjetje 1", "Podjetje 2", "Podjetje 3", "Hiša 2"];

    for (let i = 0; i < 100; i++) {
        zahtevki_test.push("Zahtevek " + i);
    }


    const addPlowClick = () => {
        fetch('http://localhost:5000/addplow', {
            method: 'POST',
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
            console.error('Error:', error);
        });
    };

    const zahtevekClicked = (key: number) => {
        alert(zahtevki_test[key]);
    }

    return (
        <div className="band">

            <div className="group">
                    <div className="top-button" onClick={addPlowClick}>Dodaj uporabnika</div>
                    <div className="top-button">Uredi štartne baze</div>
            </div>
            
            <div className="frame-2">
                <div className="rectangle">Zahtevki</div>
                <div className="zahtevki">
                        {zahtevki_test.map((item, index) => (
                            <div className="zahtevek" key={index} onClick={() => zahtevekClicked(index)}>{item}</div>
                        ))}
                </div>
            </div>
            
        </div>
    );
};

export default AdminSideBand;