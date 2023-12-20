from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .connect import sqlQuerey
import sqlite3


def index(request):
    return render(request, 'index.html')
def bell(request):
    return render(request,'bell.html')
def account(request):
    return render(request,'account.html')

def courseschedule(request):
    return render(request,'courseSchedule.html')

def product_detail(request):
    sqliteConnection = sqlite3.connect('C:\\Users\\bharal_909857\\Downloads\\Repository\\Student\\Student\\mysite\\blog\\database.db')
    try:
        output = []

        cursor = sqliteConnection.cursor()

        """
        query = '''SELECT * FROM TEACHERS'''
        cursor.execute(query)
        teacherResult = cursor.fetchall()
        for row in teacherResult:
            output.append(row)
        """
        query = '''SELECT * FROM ACC'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'ACC', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM ATH'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'Athletics', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM CTE'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'Electives', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM ENG'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'English', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM ESL'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'English Second Language', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM FINE_ART'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'Fine Arts', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM MATH'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'Math', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM SCI'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'Science', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM SOCIAL_STUDIES'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'Social Studies', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM TECH'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'Tech', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM WORLD_LANG'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'World Languages', row[1])
            output.append(new_row)
        cursor.close()
        
        

    except sqlite3.Error as error:
        print('Error occurred - ', error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            return render(request, 'courseRequests.html', {'product': output})
        
def get_classes(request):
    sqliteConnection = sqlite3.connect('C:\\Users\\bharal_909857\\Downloads\\Repository\\Student\\Student\\mysite\\blog\\database.db')
    try:
        output = []

        cursor = sqliteConnection.cursor()

        query = '''SELECT * FROM MATH'''
        cursor.execute(query)

        result = cursor.fetchall()
        for row in result:
            output.append(row)

        cursor.close()

    except sqlite3.Error as error:
        print('Error occurred - ', error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed YAY')
            return render(request, 'courseSchedule.html', {'classes': output})

