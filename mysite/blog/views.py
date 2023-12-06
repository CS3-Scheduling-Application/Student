from django.shortcuts import render, get_object_or_404
from .models import Product
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

        output = ""
        
       
        cursor = sqliteConnection.cursor()
        output += 'Connected to DataBase'

        query = '''SELECT * FROM TEACHERS'''
        cursor.execute(query)
        
        result = cursor.fetchall()
        output += 'All the data from Math table:\n'
        for row in result:
            output += str(row)+'\n'

        output += '\nColumns in TEACHERS table:' 
        data=cursor.execute('''SELECT Teacher_Name FROM TEACHERS''') 
        for column in data.description: 
            output += str(column)+'\n' 
            

        
        cursor.close()

    except sqlite3.Error as error:
        print('Error occurred - ', error)

    finally:

        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')
            product_name="test"
            return render(request, 'courseRequests.html', {'product': output})
    