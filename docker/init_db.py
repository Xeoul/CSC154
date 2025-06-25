from app import app
from models import db, User, Employee
from werkzeug.security import generate_password_hash
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create sample employee
    emp = Employee(name='John Doe', salary=60000, dob=date(1990, 1, 1), department='IT',
                   home_folder='/home/jdoe', ssn='123-45-6789')
    db.session.add(emp)
    db.session.commit()

    # Create user (employee)
    user = User(username='jdoe', password_hash=generate_password_hash('pass456'),
                role='employee', employee_id=emp.id)
    admin = User(username='admin', password_hash=generate_password_hash('password123'),
                 role='admin')

    db.session.add(user)
    db.session.add(admin)
    db.session.commit()

    print("Initialized the database with sample users.")
