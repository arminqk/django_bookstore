from django.db import models
from django.contrib.auth.models import AbstractUser , AbstractBaseUser


class CustomUser(AbstractUser): #null--->Db      #blank-->Form
    age = models.PositiveIntegerField(null=True , blank=True)







