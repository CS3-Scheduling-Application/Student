from django.contrib import admin
from django.urls import path, include
from . import views
from multiurl import ContinueResolving, multiurl

urlpatterns = [
    path('', views.index, name="index"),
    path('homepage', views.index, name="homepage"),
    path('bellSchedule', views.bell, name="bell"),
    path('account', views.account, name="account"),
    path('courseSchedule', views.courseschedule, name="courseSchedule"),
    path('courseRequests/', include([
        path('', views.product_detail, name='product_detail'),
        path('submit/', views.submit_class_requests, name='submit_class_requests'),
    ])),
]