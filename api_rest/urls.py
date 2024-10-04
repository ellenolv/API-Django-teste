from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_users, name='get_all_users'), #localhost:8000/api/
    path('user/<str:nick>', views.get_by_nick) #localhost:8000/api/user/user_name
]