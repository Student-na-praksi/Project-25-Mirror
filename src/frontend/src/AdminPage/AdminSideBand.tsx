import "./AdminSideBand-style.css";

function AdminSideBand() {

    const zahtevki_test = ["Hiša 1", "Podjetje 1", "Podjetje 2", "Podjetje 3", "Hiša 2"];

    for (let i = 0; i < 100; i++) {
        zahtevki_test.push("Zahtevek " + i);
    }


    const handleClick = () => {
        fetch('http://localhost:5000/test', {
            method: 'POST',
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
            console.error('Error:', error);
        });
    };

    return (
        <div className="band">

            <div className="group">
                    <div className="top-button" onClick={handleClick}>Dodaj uporabnika</div>
                    <div className="top-button">Uredi štartne baze</div>
            </div>
            
            <div className="frame-2">
                <div className="rectangle">Zahtevki</div>
                <div className="zahtevki">
                        {zahtevki_test.map((item, index) => (
                            <div className="zahtevek" key={index}>{item}</div>
                        ))}
                </div>
            </div>
            
        </div>
    );
};

export default AdminSideBand;