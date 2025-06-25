from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for session management

# Hardcoded users: username -> dict with password and role
users = {
    "admin": {"password": "password123", "role": "admin"},
    "jdoe": {"password": "pass456", "role": "employee"}
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def role_required(role):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'username' not in session:
                return redirect(url_for('login'))
            if session.get('role') != role:
                return "Access denied: insufficient permissions", 403
            return f(*args, **kwargs)
        return decorated_function
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = users.get(username)
        if user and user['password'] == password:
            session['username'] = username
            session['role'] = user['role']
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid username or password."

    return render_template('login.html', error=error)

@app.route('/dashboard')
@login_required
def dashboard():
    role = session.get('role')
    username = session.get('username')
    return f"Hello {username}! You are logged in with role: {role}. <br>" \
           f"<a href='/admin'>Admin Page</a> | <a href='/employee'>Employee Page</a> | <a href='/logout'>Logout</a>"

@app.route('/admin')
@login_required
@role_required('admin')
def admin_page():
    return "Welcome to the Admin Dashboard! Only admins can see this."

@app.route('/employee')
@login_required
@role_required('employee')
def employee_page():
    return "Welcome to the Employee Dashboard! Only employees can see this."

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
