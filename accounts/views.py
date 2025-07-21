from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser  # Use your custom user model


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # OPTIONAL: Get custom fields if you want to use them
        bio = request.POST.get('bio')
        location = request.POST.get('location')

        if password1 != password2:
            return render(request, 'accounts/register.html', {'error': "Passwords do not match."})

        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': "Username already exists."})

        # Create new custom user
        user = CustomUser.objects.create_user(username=username, password=password1)

        # If you want to save extra fields:
        if bio:
            user.bio = bio
        if location:
            user.location = location
        user.save()

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
