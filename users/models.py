from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import CharField


class User(AbstractUser):
    is_verified = models.BooleanField(default=False)
