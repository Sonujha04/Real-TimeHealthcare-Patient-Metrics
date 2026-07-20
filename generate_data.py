import sqlite3
import random
from datetime import datetime, timedelta
import pandas as pd
import time

# Database connect
conn = sqlite3.connect('../database/healthcare.db')
cursor = conn.cursor()

# Table create
cursor.execute('''
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    age INTEGER,
    gender TEXT,
    disease TEXT,
    department TEXT,
    admission_date TEXT,
    discharge_date TEXT,
    doctor TEXT,
    cost REAL,
    bp INTEGER,
    sugar INTEGER,
    heart_rate INTEGER
)
''')

conn.commit()

# Sample data
names = ["Amit","Ravi","Priya","Neha","Rahul"]
diseases = ["Diabetes","Heart","Fever","Covid","BP"]
departments = ["Cardiology","General","ICU","Emergency"]
doctors = ["Dr. Sharma","Dr. Khan","Dr. Singh"]

# Infinite loop for real-time data
while True:
    name = random.choice(names)
    age = random.randint(20,80)
    gender = random.choice(["Male","Female"])
    disease = random.choice(diseases)
    dept = random.choice(departments)

    admission = datetime.now() - timedelta(days=random.randint(1,5))
    discharge = admission + timedelta(days=random.randint(1,5))

    doctor = random.choice(doctors)
    cost = random.randint(2000,20000)
    bp = random.randint(90,180)
    sugar = random.randint(70,200)
    hr = random.randint(60,120)

    cursor.execute('''
    INSERT INTO patients 
    (patient_name, age, gender, disease, department, admission_date, discharge_date, doctor, cost, bp, sugar, heart_rate)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
    ''',(name,age,gender,disease,dept,admission,discharge,doctor,cost,bp,sugar,hr))

    conn.commit()

    # Export to CSV
    df = pd.read_sql_query("SELECT * FROM patients", conn)
    df.to_csv('../data/patient_data.csv', index=False)

    print("New patient added...")

    time.sleep(5)