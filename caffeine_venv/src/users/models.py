from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager



# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """
    email and password are required. Other fields are optional.
    """

    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True,
                              error_messages={
                                  'unique': _("A user with this email already exists."),
                              },
                              )
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    is_verified = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
