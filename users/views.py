from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            messages.success(request, 'Пользователь зарегистрирован')
            if user is not None:
                messages.error(request, 'Пользователь с таким именем уже существует!')
                return render(request, 'registration/signup.html', {'form': form})
            return redirect('signin')
        else:
            messages.error(request, 'Что-то пошло не так')
    return render(request, 'registration/signup.html')


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            if user is not None:
                login(user)
                messages.success(request, 'Пользователь залогинен')
                return redirect('home')
            else:
                messages.error(request, 'Неверный логин или пароль')
                return render(request, 'registration/signin.html', {'form': form})
        else:
            messages.error(request, 'Что-то пошло не так')
    return render(request, 'registration/signin.html')


def logout(request):
    pass


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'users/profile.html')

    return redirect('signup')
