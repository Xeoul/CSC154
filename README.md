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
- Backend: [Specify your backend framework/language, e.g., Python Flask, Java Spring Boot]
- Database: SQL (e.g., MySQL, PostgreSQL)
- Security: PKI certificates for HTTPS, role-based authentication
- Frontend: [Specify frontend technologies if any]

## Setup Instructions

1. **Database Setup**  
   - Create the employee database and tables as per schema.  
   - Populate initial employee and administrator data.

2. **Configure DNS**  
   - Edit `/etc/hosts` to map your domain to `127.0.0.1` or your server IP.  
   Example:  

3. **SSL/TLS Certificates**  
- Generate or obtain PKI certificates.  
- Configure the web server to use the certificates for HTTPS.

4. **Run the Application**  
- Start your backend server.  
- Access the portal at `https://secure-employee-portal.local`.

## Usage

- Employees log in to view their own profile and sensitive data.  
- Administrators log in to view and manage all employee records.

## Security Considerations

- All communication is encrypted using PKI-based SSL/TLS certificates.  
- Access control ensures data isolation between employees and administrators.

## Notes
- This project builds upon concepts from Lab 1 and Lab 2.  
- Modify the configuration files according to your environment.
