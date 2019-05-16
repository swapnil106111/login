from django.contrib import admin
from django.urls import path

from .views import loginView, signupView

urlpatterns = [
    path('login/', loginView, name='loginView'),
    path('signup/', signupView, name='signupView'),
]