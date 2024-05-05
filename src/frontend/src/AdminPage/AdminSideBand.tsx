import "./AdminSideBand-style.css";

function AdminSideBand() {
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
                    <div className="top-button" onClick={handleClick}></div>
                    <div className="top-button"></div>
            </div>
            
            <div className="frame-2">
                <div className="rectangle"></div>
                <div className="div"></div>
            </div>
            
        </div>
    );
};

export default AdminSideBand;