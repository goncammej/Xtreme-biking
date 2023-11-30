from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):

  def _create_user(self, email, name, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Los usuarios deben tener un email')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        name=name,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, name, password, **extra_fields):
    return self._create_user(email, name, password, False, False, **extra_fields)

  def create_superuser(self, email, name, password, **extra_fields):
    user=self._create_user(email, name, password, True, True, **extra_fields)
    return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Correo electrónico"), max_length=254, unique=True)
    name = models.CharField(_("Nombre completo"), max_length=254)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)