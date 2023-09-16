from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#this will make as you are logged in or logged out
from django.contrib import messages 

# Create your views here.
def home(request):
  #To check if user is logging in
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    #authenticate
    user = authenticate(request, username = username, password = password)

    if user is not None:
      login(request, user)
      messages.success(request, "You have been successfully logged in")
      return redirect('home')
    else:
      messages.success(request, 'There was an error. Please try again..')
      return redirect('home')
    
  return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')