from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Account created ! Please login.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    
    return render(request, 'login.html')

@login_required(login_url='login')
def welcome_view(request):
    return render(request, 'welcome.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')