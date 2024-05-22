from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def view_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            request.session['username'] = username
            return redirect('/')  
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html')

def view_logout(request):
    logout(request)
    if 'username' in request.session:
        del request.session['username']
    return redirect('/')

def view_register(request):
    return render(request, 'register.html')

def view_changepassword(request):
    return render(request, 'changepassword.html')