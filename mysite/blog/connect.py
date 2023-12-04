import sqlite3

try:

    sqliteConnection = sqlite3.connect('mysite/blog/database.db')
    cursor = sqliteConnection.cursor()
    print('Connected to DataBase')

    query = '''SELECT * FROM TEACHERS'''
    cursor.execute(query)
    
    result = cursor.fetchall()
    print('All the data from Math table:')
    for row in result:
        print(row)

    print('\nColumns in TEACHERS table:') 
    data=cursor.execute('''SELECT Teacher_Name FROM TEACHERS''') 
    for column in data.description: 
        print(column) 
        

    
    cursor.close()

except sqlite3.Error as error:
    print('Error occurred - ', error)

finally:

    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')