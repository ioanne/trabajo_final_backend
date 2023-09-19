from django.db import models


class Inventary(models.Model):
    character = models.ForeignKey("character.Character", on_delete=models.CASCADE)
    item = models.ForeignKey("item.Item", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)
