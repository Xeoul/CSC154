from app import app
from models import db, User, Employee
from werkzeug.security import generate_password_hash
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create admin user
    admin = User(username='admin', password_hash=generate_password_hash('password123'), role='admin')
    db.session.add(admin)

    # Create random employees and associated users
    emp0 = Employee(name='Patricia Barry', salary=119483.24, dob=date(1963, 12, 6),
                     department='IT', home_folder='/home/patriciabarry', ssn='431-68-9098')
    db.session.add(emp0)
    db.session.flush()  # flush to get emp0.id
    
    emp1 = Employee(name='Jerry Robinson', salary=110121.05, dob=date(1977, 4, 23),
                     department='Marketing', home_folder='/home/jerryrobinson', ssn='693-99-1798')
    db.session.add(emp1)
    db.session.flush()  # flush to get emp1.id
    
    emp2 = Employee(name='Mikayla Harper', salary=75660.38, dob=date(1962, 3, 24),
                     department='Marketing', home_folder='/home/mikaylaharper', ssn='631-22-8755')
    db.session.add(emp2)
    db.session.flush()  # flush to get emp2.id
    
    emp3 = Employee(name='Michelle Wong', salary=66270.06, dob=date(1983, 8, 29),
                     department='HR', home_folder='/home/michellewong', ssn='495-79-6619')
    db.session.add(emp3)
    db.session.flush()  # flush to get emp3.id
    
    emp4 = Employee(name='Anthony Potter', salary=90186.64, dob=date(1988, 2, 20),
                     department='IT', home_folder='/home/anthonypotter', ssn='202-73-4804')
    db.session.add(emp4)
    db.session.flush()  # flush to get emp4.id
    
    emp5 = Employee(name='Loretta Sherman', salary=54988.15, dob=date(1982, 1, 13),
                     department='HR', home_folder='/home/lorettasherman', ssn='657-12-9444')
    db.session.add(emp5)
    db.session.flush()  # flush to get emp5.id
    
    emp6 = Employee(name='Tracy Chaney', salary=41781.66, dob=date(1979, 3, 18),
                     department='HR', home_folder='/home/tracychaney', ssn='228-71-7139')
    db.session.add(emp6)
    db.session.flush()  # flush to get emp6.id
    
    emp7 = Employee(name='Lisa Murphy', salary=54840.0, dob=date(1992, 6, 21),
                     department='Sales', home_folder='/home/lisamurphy', ssn='186-01-9205')
    db.session.add(emp7)
    db.session.flush()  # flush to get emp7.id
    
    emp8 = Employee(name='Jenny Farley', salary=82243.7, dob=date(1993, 10, 18),
                     department='Finance', home_folder='/home/jennyfarley', ssn='543-47-3762')
    db.session.add(emp8)
    db.session.flush()  # flush to get emp8.id
    
    emp9 = Employee(name='Alexander Brown', salary=75863.31, dob=date(1973, 2, 26),
                     department='Sales', home_folder='/home/alexanderbrown', ssn='405-72-9658')
    db.session.add(emp9)
    db.session.flush()  # flush to get emp9.id
    
    user0 = User(username='patricia0', password_hash=generate_password_hash('pass100'),
                  role='employee', employee_id=emp0.id)
    db.session.add(user0)
    
    user1 = User(username='jerry1', password_hash=generate_password_hash('pass101'),
                  role='employee', employee_id=emp1.id)
    db.session.add(user1)
    
    user2 = User(username='mikayla2', password_hash=generate_password_hash('pass102'),
                  role='employee', employee_id=emp2.id)
    db.session.add(user2)
    
    user3 = User(username='michelle3', password_hash=generate_password_hash('pass103'),
                  role='employee', employee_id=emp3.id)
    db.session.add(user3)
    
    user4 = User(username='anthony4', password_hash=generate_password_hash('pass104'),
                  role='employee', employee_id=emp4.id)
    db.session.add(user4)
    
    user5 = User(username='loretta5', password_hash=generate_password_hash('pass105'),
                  role='employee', employee_id=emp5.id)
    db.session.add(user5)
    
    user6 = User(username='tracy6', password_hash=generate_password_hash('pass106'),
                  role='employee', employee_id=emp6.id)
    db.session.add(user6)
    
    user7 = User(username='lisa7', password_hash=generate_password_hash('pass107'),
                  role='employee', employee_id=emp7.id)
    db.session.add(user7)
    
    user8 = User(username='jenny8', password_hash=generate_password_hash('pass108'),
                  role='employee', employee_id=emp8.id)
    db.session.add(user8)
    
    user9 = User(username='alexander9', password_hash=generate_password_hash('pass109'),
                  role='employee', employee_id=emp9.id)
    db.session.add(user9)
    

    db.session.commit()
    print("Initialized the database with 10 random employees and 1 admin.")
