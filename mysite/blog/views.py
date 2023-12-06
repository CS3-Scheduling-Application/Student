from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse
from .connect import sqlQuerey

def index(request):
    return render(request, 'index.html')
def bell(request):
    return render(request,'bell.html')
def account(request):
    return render(request,'account.html')
def courserequests(request):
    return render(request,'courseRequests.html')
def courseschedule(request):
    return render(request,'courseSchedule.html')

def course_requests(request):
    try:
        result = sqlQuerey()  # Call the function from connect.py
        # You can pass 'result' to your template context if you want to display it in the HTML

        return render(request, 'courseRequests.html', {'result': result})

    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")

