from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .connect import sqlQuerey
from multiurl import ContinueResolving
import sqlite3
import os


def index(request):
    return render(request, 'index.html')
def bell(request):
    return render(request,'bell.html')
def account(request):
    return render(request,'account.html')

def courseschedule(request):
    return render(request,'courseSchedule.html')


def get_course_catalog(request):
    sqliteConnection = sqlite3.connect('database.db')
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
            new_row = (row[0], 'ACC', 'ACC', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM ATH'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'ATH', 'Athletics', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM CTE'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'CTE', 'Electives', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM ENG'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'ENG', 'English', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM ESL'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'ESL', 'English Second Language', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM FINE_ART'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'FINE_ART', 'Fine Arts', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM MATH'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'MATH', 'Math', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM SCI'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'SCI', 'Science', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM SOCIAL_STUDIES'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'SOCIAL_STUDIES', 'Social Studies', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM TECH'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'TECH', 'Tech', row[1])
            output.append(new_row)
        
        
        query = '''SELECT * FROM WORLD_LANG'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            new_row = (row[0], 'WORLD_LANG', 'World Languages', row[1])
            output.append(new_row)
        cursor.close()
        
        

    except sqlite3.Error as error:
        print('Error occurred - ', error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            return render(request, 'courseRequests.html', {'product': output})

def submit_class_requests(request):
    print("HELLO")
    if request.method == 'POST':
        # Assuming 'class_select1' is the name attribute of your <select> element
        classes= []
        for i in range(11):
            classes.append(request.POST.get('class_select_'+str(i+1)))
             

        # Now 'class_one_value' contains the selected value from the form
        print(f"Selected value for classes: {classes}")

        # Assuming you need to pass some data to the template, create a context dictionary
        context = {
            'selected_class': classes,
            # Add other data you want to pass to the template
        }

        # Render the template with the context
        return render(request, 'courseRequests.html', context)

    # Handle other HTTP methods or return a response for GET requests if needed
    # ...

