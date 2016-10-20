from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


# Account model's manager
class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username')

        account = self.model(
            email=self.normalize_email(email),
            username=kwargs.get('username')
            )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account

# Our Account model for logging-in
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
