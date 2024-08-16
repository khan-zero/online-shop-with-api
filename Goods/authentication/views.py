from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            text = "This username is already taken"
            return render(request, 'error.html', {'message': text})

        User.objects.create_user(
            username=username,
            password=request.POST['password'],
            email=request.POST['email']
        )
        return redirect('login')

    return render(request, 'login-register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'error.html', {'message': 'Invalid credentials'})

    return render(request, 'login-register.html')


def log_out(request):
    logout(request)
    return redirect('index')

def error(request):
    return render(request, 'error.html')
