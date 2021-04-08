import sqlite3

try:
    conn = sqlite3.connect('students_record.db')
    print('connection Successful')
    conn.execute("CREATE TABLE students(id INT PRIMARY KEY, names TEXT NOT NULL, marks TEXT NOT NULL, grades TEXT NOT NULL)")
    conn.close()
except ConnectionError:
    print("connection refused")
