from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=50)

    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    tagline = models.CharField(blank=True, max_length=150)

    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        return self.email

    def get_fullname(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name
