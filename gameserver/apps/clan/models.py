from django.db import models


class Clan(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    nivel = models.PositiveIntegerField(default=1)
    # El releated name es como vas a ver la relacion en character en este caso
    # lo vamos a ver como clan_leader
    leader = models.OneToOneField(
        "character.Character", on_delete=models.DO_NOTHING, related_name="clan_leader"
    )

    # Dependiendo el nivel del clan
    # es la cantidad de miembros que puede tener
    def save(self, *args, **kwargs):
        self.id
        # Chequear si el miembro que se inscribe ya tiene clan
        # Chequear si hay lugar en el clan
        super().save(*args, **kwargs)

        # Si es un clan nuevo, crear el clan member del lider
        if self.id is None:
            ClanMember.objects.create(
                character=self.leader, clan_id=self.id, title="Lider"
            )

    def __str__(self):
        return f"{self.name}({self.id}) - {self.nivel}"

    @classmethod
    def get_cosas(
        cls,
        nivel_leader,
        nivel_clan,
        leader_inventary_item_name,
        leader_inventary_equipped,
    ):
        cls.objects.filter(
            leader__nivel__gte=nivel_leader,
            nivel=nivel_clan,
            leader__inventary__item__name=leader_inventary_item_name,
            leader__inventary__equipped=leader_inventary_equipped,
        )


class ClanMember(models.Model):
    character = models.ForeignKey(
        "character.Character", on_delete=models.CASCADE, related_name="clan_member"
    )
    clan = models.ForeignKey(
        "clan.Clan", on_delete=models.CASCADE, related_name="members"
    )
    title = models.CharField(max_length=50)

    # El clan member no se deberia poder borrar si es lider del clan.


"""
Query compleja:
Clan.objects.filter(
    leader__nivel__gte=10,
    nivel=1,
    leader__inventary__item__name='pepe',
    leader__inventary__equipped=True,
    leader=character
)
"""
