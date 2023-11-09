from django.shortcuts import render
from django.http import HttpResponse
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