from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data.get('username'),
                                            password=form.cleaned_data.get('password'))
            messages.success(request, 'Пользователь зарегистрирован')
            return redirect('signin')
        else:
            messages.error(request, 'Что-то пошло не так')
    return render(request, 'registration/signup.html')


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.validate_username():
            user = authenticate(username=form.data.get('username'),
                                password=form.data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Неверный логин или пароль')
                return render(request, 'registration/signin.html', {'form': form})
        else:
            messages.error(request, 'Что-то пошло не так')
    return render(request, 'registration/signin.html')


def logout_(request):
    logout(request)
    return redirect('home')


def profile(request):
    if request.user.is_authenticated:
        data = {
            'username': request.user.username
        }
        return render(request, 'users/profile.html', data)

    return redirect('signup')
