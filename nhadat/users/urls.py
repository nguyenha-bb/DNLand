from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('login',views.view_login, name='login'),
    path('logout', views.view_logout, name='logout'),
    path('register',views.view_register, name='register'),
    path('change-password',views.view_changepassword, name='change-password')
]
