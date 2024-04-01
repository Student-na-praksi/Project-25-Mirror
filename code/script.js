//JAVASCRIPT
// const express = require('express');
// const mysql = require('mysql');
// import mysql.connector

// // Import the required modules

// // Create a connection to the MySQL database
// const connection = mysql.createConnection({
//     host: 'localhost',
//     user: 'your_username',
//     password: 'your_password',
//     database: 'your_database_name'
// });

// // Create an Express application
// const app = express();

// // Configure the Express application
// app.use(express.urlencoded({ extended: false }));
// app.use(express.json());

// // Handle the register endpoint
// app.post('/register', (req, res) => {
//     const { username, password } = req.body;

//     // Insert the user into the database
//     const query = `INSERT INTO users (username, password) VALUES (?, ?)`;
//     connection.query(query, [username, password], (error, results) => {
//         if (error) {
//             console.error('Error registering user:', error);
//             res.status(500).json({ error: 'An error occurred while registering the user' });
//         } else {
//             res.status(200).json({ message: 'User registered successfully' });
//         }
//     });
// });

// // Handle the button click endpoint
// app.post('/button-click', (req, res) => {
//     // Perform the desired action when the button is clicked
//     // For example, update a value in the database or trigger some other functionality

//     res.status(200).json({ message: 'Button clicked successfully' });
// });

// // Start the server
// app.listen(3000, () => {
//     console.log('Server is running on port 3000');
// });
// from flask import Flask, request, jsonify
