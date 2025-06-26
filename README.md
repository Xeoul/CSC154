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
           Nginx
- Database: PostgreSQL (via Docker)
- Security: PKI certificates for HTTPS, role-based authentication
- Frontend: Flask Jinja2 templates for UI

## Setup Instructions

1. **VM setup instruction**  
   - Modify the host file /etc/hosts
   - Add "127.0.0.1 www.project154.com" to the hosts file

2. **Running with Docker**
   - We use Docker and Docker Compose to run PostgreSQL, Nginx and the Flask backend.
   - Make sure Docker is installed and running.  
   - From the project folder (where `docker-compose.yml` is), run:  
     ```bash
     docker-compose up --build
     docker-compose exec backend python init_db.py
     ```  
   - Access the app at:  
     ```
     https:www.project154.com/
     ```
3. **(If necessary) Import Root CA into Firefox 
   - Open Firefox
   - Go to Settings -> Privacy & Security -> View Certificates
   - Tab: Authorities
   - Click Import
   - Choose ca/certs/rootCA.pem
   - Check "Trust this CA to identify websites"
   - Click OK and restart Firefox
     
4. **Login Page**  
   - Use one of the example credentials found in the init_dp.py to login.
   - Successful login shows a welcome message; invalid login shows an error.

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
- [x] Add SSL/TLS certificates for HTTPS  
- [x] Employee data views per role
- [x] Working Database
