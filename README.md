# Secure Employee Portal

## Project Overview
This web application provides secure access to an employee database containing sensitive information such as name, salary, date of birth, department, home folder, and SSN. The system ensures data privacy by restricting employees to view only their own information, while administrators have full access to all employee data.

## Features
- Secure login for employees and administrators
- Role-based access control (employee vs administrator)
- Employee data stored in a SQL database
- PKI-based SSL/TLS certificates for secure HTTPS access
- DNS configured via `/etc/hosts` for local domain resolution

## Technologies Used
- Backend: Python Flask
- Database: PostgreSQL (via Docker)
- Security: PKI certificates for HTTPS, role-based authentication (in progress)
- Frontend: Flask Jinja2 templates for UI

## Setup Instructions

1. **Database and Backend Setup**  
   - We use Docker and Docker Compose to run PostgreSQL and the Flask backend together.  
   - Create a folder structure and files as per the project (see Dockerfile, docker-compose.yml, app.py).  
   - Flask app currently includes a simple login page with hardcoded users.

2. **Running with Docker**  
   - Make sure Docker is installed and running.  
   - From the project folder (where `docker-compose.yml` is), run:  
     ```bash
     docker-compose up --build
     ```  
   - Access the app at:  
     ```
     http://localhost:5000/login
     ```

3. **Login Page**  
   - Use one of the hardcoded credentials to log in:  
     - admin / password123  
     - jdoe / pass456  
   - Successful login shows a welcome message; invalid login shows an error.

4. **Next Steps**  
   - Expand the login system with database authentication.  
   - Implement role-based access control.  
   - Add SSL/TLS certificates for HTTPS (optional for local dev).  
   - Develop full employee data views based on user role.

## Security Considerations
- All communication should eventually be encrypted with PKI-based SSL/TLS certificates.  
- Role-based access ensures users only see authorized data.  
- Passwords should be hashed before storing in a database (future work).

## Notes
- This project is built on concepts from Lab 1 and Lab 2.  
- Modify configuration files according to your environment.

## Progress

- [x] Implement login page  
- [x] Implement RBAC (role-based access control)  
- [ ] Add SSL/TLS certificates for HTTPS  
- [ ] Employee data views per role
- [ ] Working Database
