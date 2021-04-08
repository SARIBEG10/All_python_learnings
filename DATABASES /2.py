import sqlite3


conn = sqlite3.connect('students_record.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO students (id, grades, marks, names) VALUES (?, ?, ?, ?)", (1, 'A', '100', 'stewart'))
conn.commit()
conn.close()

