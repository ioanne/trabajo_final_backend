from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    phone = models.CharField(max_length=20)

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class CustomUser(AbstractUser):
    # objects_all = models.Manager()
    # objects = CustomUserManager()
    pass


# # Ejemplo de uso

# # users = CustomUser.objects.all()
