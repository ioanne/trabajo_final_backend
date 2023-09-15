from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=16)
    # El null true y blank true hacen que pueda estar nulo o vacio.
    title = models.CharField(max_length=25, null=True, blank=True)
    nivel = models.PositiveIntegerField()
