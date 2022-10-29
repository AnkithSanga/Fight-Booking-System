from django.contrib import admin
from django.urls import path, include
from Bookings import views
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home,name='Home'),
]