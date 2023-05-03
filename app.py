from flask import Flask, request
from sqlalchemy import create_engine, Column, Integer, String, DateTime, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER
from queries import DATA_Q, LIST_ID

# Declare the Base class for creating declarative entities
Base = declarative_base()

# Defining the classes
class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    department = Column(String)

class Employee(Base):
    __tablename__ = 'hired_employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    datetime = Column(String)
    department_id = Column(Integer)
    job_id = Column(Integer)

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    job = Column(String)

# Creating the engine to connnect with ElephantSQL
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
#Base.metadata.create_all(engine)

# Create a session factory to manage the pool connections
Session = sessionmaker(bind=engine)

# Create the flaskk app
app = Flask(__name__)

#Create end point part 2 of the challenge
@app.route('/data_q', methods=['GET'])
def get_data_q():
    query_data = text(DATA_Q)
    session = Session()
    query = session.execute(query_data)
    session.close() # Close the session
    
    query_restult = [] # Set the result like a json response
    for i in query:
        query_restult.append({
            'department': i[0],
            'job': i[1],
            'Q1': i[2],
            'Q2': i[3],
            'Q3': i[4],
            'Q4': i[5]
        })
    return query_restult


#Create end point part 2 of the challenge
@app.route('/list_id', methods=['GET'])
def get_list_d():
    query_data = text(LIST_ID)
    session = Session()
    query = session.execute(query_data)
    session.close() # Close the session
    
    query_result = [] # Set the result like a json response
    for i in query:
        query_result.append({
            'id': i[0],
            'department': i[1],
            'hired': i[2]
        })

    return query_result

#endpont of firts part
@app.route('/upload', methods=['POST'])
def upload():

    # Check if any of the csv files exists
    if 'departments' in request.files:
        departments = request.files['departments'] # obtain the file object of the request
        data = departments.read().decode('utf-8').splitlines()
        session = Session() # Creando una sesion
        for line in data:
            department_id, department = line.split(';')
            session.add(Department(id=department_id, department=department))
        session.commit() # Commit the changes to the database
        session.close() ## Close connection

    if 'hired_employees' in request.files:
        hired_employees = request.files['hired_employees']
        data = hired_employees.read().decode('utf-8').splitlines()
        session = Session()
        for line in data:
            employee_id, name, datetime, department_id, job_id = line.split(';')
            try:
                department_id = int(department_id) # Check if the the column as a integer, if not, set a none value
            except ValueError:
                department_id = None
            try:
                job_id = int(job_id) # Check id the column as a integer, if not set a none value
            except ValueError:
                job_id = None
            session.add(Employee(id=employee_id, name=name, datetime=datetime, department_id=department_id, job_id=job_id))
        session.commit() # Commit the changes to the database
        session.close() ## Close connection

    if 'jobs' in request.files:
        jobs = request.files['jobs']
        data = jobs.read().decode('utf-8').splitlines()
        session = Session()
        for line in data:
            job_id, job = line.split(';')
            session.add(Job(id=job_id, job=job))
        session.commit()
        session.close()

    return 'Files were uploaded correctly'

if __name__ == '__main__':
    app.run(debug=True)
