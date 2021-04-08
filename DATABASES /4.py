import sqlite3


conn = sqlite3.connect('students_record.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM students")

all_data = cursor.fetchone()
for data in all_data:
    print(data)






