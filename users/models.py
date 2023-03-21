from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone_number, first_name, last_name, password):
        if not email:
            raise ValueError('Users must have an email')
        if not phone_number:
            raise ValueError('Users must have an phone number')
        if not first_name:
            raise ValueError('Users must have an first name')
        if not last_name:
            raise ValueError('Users must have an last name')
        if not password:
            raise ValueError('Users must have an password')

        user = self.model(
            email=self.normalize_email(email=email),
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(raw_password=password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, first_name, last_name, password):
        user = self.create_user(
            email=email,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=40, unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    phone_number = PhoneNumberField(max_length=13, default='+996', null=True, unique=True,
                                    verbose_name='Номер телефона', )
    password = models.CharField(max_length=50, verbose_name='Пароль')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'first_name', 'last_name', 'password']

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
