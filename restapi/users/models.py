from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, blank=True)
    login = models.CharField(max_length=255, unique=True, blank=True)
    phone = models.IntegerField(blank=True)
    tg = models.CharField(max_length=255)
    birth = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['name', 'password', 'birth', 'email', 'phone']

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)

        now = timezone.now()
        if (now.year - self.dob.year) > 18:
            raise ValidationError('Вы должны быть совершеннолетним')
