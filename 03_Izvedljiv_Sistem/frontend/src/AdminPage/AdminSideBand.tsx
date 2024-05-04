import "./AdminSideBand-style.css";
import React from 'react';

function AdminSideBand() {
    const handleLoginClick = () => {
        fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json', // Set the appropriate content type
            },
            body: JSON.stringify(requestData), // Convert data to JSON format
        })
            .then((response) => {
                if (response.ok) {
                    // Handle successful response (e.g., redirect, show success message)
                    console.log('Login successful');
                } else {
                    // Handle error response (e.g., display error message)
                    console.error('Login failed');
                }
            })
            .catch((error) => {
                console.error('Error during login:', error);
            });
        console.log('Login button clicked');
        // Replace the console.log with your actual login API call
    };

    const handleRegisterClick = () => {
        fetch('/api/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json', // Set the appropriate content type
            },
            body: JSON.stringify(requestData), // Convert data to JSON format
        })
            .then((response) => {
                if (response.ok) {
                    // Handle successful response (e.g., redirect, show success message)
                    console.log('Registration successful');
                } else {
                    // Handle error response (e.g., display error message)
                    console.error('Registration failed');
                }
            })
            .catch((error) => {
                console.error('Error during registration:', error);
            });
        
        // Call your register API here
        console.log('Register button clicked');
        // Replace the console.log with your actual register API call
    };

    const requestData = {
        username: 'test1',
        password: 'test1',
        // Add other relevant data here
    };

    return (
        <div className="band">
            <div className="group">
                <button className="top-button" onClick={handleLoginClick}>
                    Login
                </button>
                <button className="top-button" onClick={handleRegisterClick}>
                    Register
                </button>
            </div>
            <div className="frame-2">
                <div className="rectangle"></div>
                <div className="div"></div>
            </div>
        </div>
    );
};

export default AdminSideBand;

// Assuming you're running this JavaScript code in a browser environment

// Define the data you want to send (if needed)


// Make a POST request to your Flask route
