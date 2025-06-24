from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded users for testing: username -> password
users = {
    "admin": "password123",
    "jdoe": "pass456"
}

@app.route('/')
def home():
    return "Secure Employee Portal is running!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and users[username] == password:
            return f"Login successful! Welcome, {username}."
        else:
            error = "Invalid username or password."

    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
