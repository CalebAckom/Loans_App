from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, phone_number='',
                    password=None,
                    ):

        """
        Creates and saves a User with the given email and password.
        """

        user = self.model(phone_number=phone_number)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            phone_number,
            password=password,
        )
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser):
    user_key = models.UUIDField(
        unique=True,
        primary_key=True,
    )

    is_admin = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True,
    )

    registration_date = models.DateTimeField(
        auto_now_add=True
    )

    phone_number = models.CharField(
        max_length=255,
        blank=True,
        unique=True
    )

    first_name = models.CharField(
        max_length=255,
        blank=True,
    )

    last_name = models.CharField(
        max_length=255,
        blank=True,
    )

    staff_id = models.CharField(
        max_length=255,
        blank=True,
    )

    sms_confirm_code = models.CharField(
        max_length=255,
        blank=True,
    )
    is_deleted = models.BooleanField(
        default=False
    )

    # unique field
    USERNAME_FIELD = 'phone_number'
    objects = UserManager()
