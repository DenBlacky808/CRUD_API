from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class User(models.Model):
    username = models.CharField(verbose_name='Username', max_length=150)
    first_name = models.CharField(verbose_name='FirstName', max_length=30)
    last_name = models.CharField(verbose_name='LastName', max_length=150)
    is_active = models.BooleanField(verbose_name='Active')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
