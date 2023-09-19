from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=16)
    # El null true y blank true hacen que pueda estar nulo o vacio.
    title = models.CharField(max_length=25, null=True, blank=True)
    nivel = models.PositiveIntegerField()

    def get_clan(self):
        return self.clan_member.first()

    @property
    def member(self):
        return self.clan_member.first()

    @property
    def clan(self):
        clan_member = self.get_clan()
        return clan_member.clan if clan_member else None

    def __str__(self) -> str:
        return f"{self.name}({self.id}) - {self.nivel}"
