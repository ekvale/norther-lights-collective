from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/card/sign-in.html', {'form': form})

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to home page after registration
    else:
        form = SignUpForm()
    return render(request, 'authentication/card/sign-up.html', {'form': form})

def sign_out(request):
    logout(request)
    return redirect('sign_in')  # Redirect to sign-in page after logout

def reset_password(request):
    return render(request, 'authentication/card/reset-password.html')

def forgot_password(request):
    return render(request, 'authentication/card/forgot-password.html')

def lock_screen(request):
    return render(request, 'authentication/card/lock-screen.html')

def two_fa(request):
    return render(request, 'authentication/card/2FA.html')
