# Импортируем из django models для работы с моделями.
from django.db import models
# Импортируем из django AbstractUser для расширения пользователей.
from django.contrib.auth.models import AbstractUser


# Создадим класс User, который наследует AbstractUser.
class User(AbstractUser):
    # Создадим поле username с максимальной длинной 255.
    username = models.CharField(max_length=150)
    # Создадим поле email с максимальной длинной 255, и которое является уникальным.
    email = models.CharField(max_length=150, unique=True)
    # Создадим поле password с максимальной длинной 255.
    password = models.CharField(max_length=150)
    # Имя пользователя будет заменяться email.
    USERNAME_FIELD = 'email'
    # Cписок имен полей, которые будут запрашиваться при создании пользователя с помощью createsuperuser.
    REQUIRED_FIELDS = ['username']
