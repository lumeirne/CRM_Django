from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
#this will make as you are logged in or logged out
from django.contrib import messages 

# Create your views here.
def home(request):
  return render(request, 'home.html', {})