from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    stackable = models.BooleanField(default=False)
