// FRONTEND JAVASCRIPT THAT HANDLES FORMS

//pack data into json and send it to the server for login
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: document.getElementById('loginUsername').value,
            password: document.getElementById('loginPassword').value
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Login response:", data)
        document.getElementById('loginStatus').textContent = data.message;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

//pack data into json and send it to the server for register
document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: document.getElementById('registerUsername').value,
            password: document.getElementById('registerPassword').value
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Register response:", data)
        document.getElementById('registerStatus').textContent = data.message;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});

//show/hide password on eye click
document.querySelectorAll(".toggle-password").forEach(function(element) {
    element.addEventListener("click", function() {
        console.log("Eye icon clicked"); // Log the click event
        element.classList.toggle("fa-eye");
        element.classList.toggle("fa-eye-slash");
        var input = document.querySelector(element.getAttribute("toggle"));
        if (input.getAttribute("type") === "password") {
            input.setAttribute("type", "text");
        } else {
            input.setAttribute("type", "password");
        }
    });
});