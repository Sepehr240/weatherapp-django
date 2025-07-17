from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'accounts/register.html', {'error': "Passwords do not match."})

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': "Username already exists."})

        User.objects.create_user(username=username, password=password1)
        return redirect('login')

    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {'error': "Invalid credentials."})

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')
