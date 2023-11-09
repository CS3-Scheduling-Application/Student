from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('homepage', views.index, name="homepage"),
    path('bellSchedule', views.bell, name="bell"),
    path('account', views.account, name="account"),
    path('courseSchedule', views.courseschedule, name="courseSchedule"),
    path('courseRequests', views.courserequests, name="courseRequests"),
]