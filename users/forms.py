from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.core.files.images import get_image_dimensions


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
    username = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ['password']

    def clean_username(self) -> str:
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise ValidationError('Пользователя с таким именем не существует!')
        return username


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'image']

    def validate_image(self) -> bool:
        image = self.files.get('image')

        if image is None:
            return True

        try:
            width, height = get_image_dimensions(image)

            # validate dimensions
            max_width = max_height = 200
            if width > max_width or height > max_height:
                self.add_error('image', f'Используйте изображение {max_width} x {max_height} пикселей или меньше!')
                return False

            # validate content type
            main, sub = image.content_type.split('/')
            if not (main == 'image' and sub in {'jpeg', 'pjpeg', 'png'}):
                self.add_error('image', 'Используйте JPEG или PNG формат!')
                return False

        except AttributeError:
            """
            Handles case when we are updating the users profile
            and do not supply a new avatar
            """
            pass

        return True
