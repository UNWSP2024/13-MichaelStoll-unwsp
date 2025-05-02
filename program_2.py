#title: Cities
#author: michael stoll
#date: 5/2/25
import sqlite3
connect = sqlite3.connect('cities.db')
cursor = connect.cursor()

cursor.execute('SELECT * FROM Cities')
results = cursor.fetchall()

print('Contents of cities.db/Cities table:')
for row in results:
    print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}')

connect.close()
