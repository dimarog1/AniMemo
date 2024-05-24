from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Пользователь с таким именем уже существует!')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        validate_password(password)
        return password


class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def validate_username(self):
        username = self.data['username']
        if not User.objects.filter(username=username).exists():
            raise ValidationError('Пользователя с таким именем не существует!')
        return username

    def clean_username(self):
        username = self.cleaned_data['username']
        x = User.objects.all()
        for elem in x:
            print(elem.username, elem.password)
        if not User.objects.filter(username=username).exists():
            raise ValidationError('Пользователя с таким именем не существует!')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        validate_password(password)
        return password
