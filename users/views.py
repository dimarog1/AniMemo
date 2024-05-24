from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.contrib.auth import authenticate, login, logout
from .models import User


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data.get('username'),
                                            password=form.cleaned_data.get('password'))
            return redirect('signin')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    return render(request, 'registration/signup.html')


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.data.get('username'),
                                password=form.data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error('username', 'Неверный пароль!')
                return render(request, 'registration/signin.html', {'form': form})
        else:
            return render(request, 'registration/signin.html', {'form': form})
    return render(request, 'registration/signin.html')


def logout_(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    return render(request, 'users/profile.html')
