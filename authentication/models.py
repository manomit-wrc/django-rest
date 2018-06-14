from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        # Ensure that an email address is set
        if not email:
            raise ValueError('Users must have a valid e-mail address')

        # Ensure that a username is set
        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username')

        account = self.model(
            email=self.normalize_email(email),
            username=kwargs.get('username'),
            firstname=kwargs.get('firstname', None),
            lastname=kwargs.get('lastname', None),
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password=None, **kwargs):
        account = self.create_user(email, password, kwargs)

        account.is_admin = True
        account.save()

        return account


class Account(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True)

    firstname = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return ' '.join(self.firstname, self.last_login)


class Publish(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    uid = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

class PublishAsset(models.Model):
    publish = models.ForeignKey(Publish, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    uid = models.CharField(max_length=150)
    url = models.CharField(max_length=255)
    type_of_assets = models.CharField(max_length=50, default='TVSHOW')

class Schedule(models.Model):
    title = models.CharField(max_length=150)
    uid = models.CharField(max_length=150)
    start_at = models.DateTimeField(auto_now_add=True)
    is_loop = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_schedule = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
