from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser
)
# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self,email,is_owner=False, is_client=False, first_name= None ,last_name=None, password=None):
        if not email:
            raise ValueError("user must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            is_owner=is_owner,
            is_client=is_client,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password=None):
        user = self.create_user(
            email, password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(
        default=True,
        verbose_name='email address',
        max_length=225,
        unique=True,
     )
    first_name = models.CharField(
        max_length=100,
        verbose_name='first_name',
        default=None,
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='last_name',
        default=None,
    )
    is_owner = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin