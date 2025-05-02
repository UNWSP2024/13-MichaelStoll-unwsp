#title: Phonebook
#author: michael stoll
#date: 5/2/25
import sqlite3

connect = sqlite3.connect('phonebook.db')
cursor = connect.cursor()

def display():
    cursor.execute('SELECT * FROM phonebook')
    results = cursor.fetchall()

    print('Contents of phonebook.db/phonebook table:')
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:.0f}')

def delete_data():
    display()
    del_row = int(input('Which row will be deleted?:'))
    try:
        cursor.execute("DELETE FROM phonebook WHERE EntryID = ?", (del_row,))
        connect.commit()
        print("Record deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting data: {e}")

def update_data():
    display()
    update_row = int(input('Which row will be updated?:'))
    name_or_num = str(input('Update name or number?:' ))
    if name_or_num == 'name':
        try:
            update_name = str(input('What is the new name?:'))
            cursor.execute("UPDATE phonebook SET Name = ? WHERE EntryID = ?", (update_name, update_row))
            connect.commit()
            print("Record updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating data: {e}")
    elif name_or_num == 'number':
        try:
            update_phone_num = int(input('What is the new phone number?:'))
            cursor.execute("UPDATE phonebook SET PhoneNumber = ? WHERE EntryID = ?", (update_phone_num, update_row))
            connect.commit()
            print("Record updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating data: {e}")
    else:
        print('Invalid row.')

decision = str(input('What do you want to do? delete, update, or read: '))
if decision == 'delete':
    delete_data()
    display()
elif decision == 'update':
    update_data()
    display()
elif decision == 'read':
    display()
else:
    print('Invalid choice')
connect.close()