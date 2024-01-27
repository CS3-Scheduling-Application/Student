from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('homepage', views.index, name="homepage"),
    path('bellSchedule', views.bell, name="bell"),
    path('account', views.account, name="account"),
    path('courseSchedule', views.courseschedule, name="courseSchedule"),
    path('courseRequests', views.get_course_catalog, name='get_course_catalog'),
    path('Sad', views.submit_class_requests, name='submit_class_requests')
]