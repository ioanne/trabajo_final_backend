from django.db import models
from django.db.models import Q


class CharacterManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(banned=False)


class Character(models.Model):
    name = models.CharField(max_length=16)
    # El null true y blank true hacen que pueda estar nulo o vacio.
    title = models.CharField(max_length=25, null=True, blank=True)
    nivel = models.PositiveIntegerField()
    banned = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)

    objects = CharacterManager()
    objects_all = models.Manager()

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


"""
    Como creamos un registro en django:
    character = Character(name="Gandalf", nivel=1)
    character.save()

    Tambien podemos hacerlo usando el manager y no hace flta hacer save.
    character = Character.objects.create(name="Gandalf", nivel=1)

    Como editar un registro en django:
    
    Ojo al obtener el objeto, el metodo get FALLA si no existe el id y da una excepcion de tipo DoesNotExist.
    character = Character.objects.get(id=1)

    Una manera segura de obtener el objeto es usando un try except:
    try:
        Character.objects.get(id=10)
    except Character.DoesNotExist:
        print('El usuario no existe')

    La otra manera es usando el metodo filter, que devuelve una lista vacia si no encuentra nada.
    Y podemos usar el fist() que si es una lista vacia, devuelve None.
    Character.objects.filter(id=1).first()


    Filter --> Incluye los que cumplen la condicion
    Exclude --> Excluye los que cumplen la condicion


    Si quiero obtener todos los character de nivel 10 o mas:
    Character.objects.filter(nivel__gte=10)
    gte = greater than or equal
    lte = less than or equal
    gt = greater than
    lt = less than

    Si quiero obtener todos los character que empiezan con el nombre Admin
    Character.objects.filter(name__startswith="Admin")
    
    Si quiero obtener todos los character que contengan el nombre Admin
    Character.objects.filter(name__contains="Admin")

    Si quiero obtener todos los character que terminen con el nombre Admin
    Character.objects.filter(name__endswith="Admin")

    
    from django.db.models import Q
    Character.objects.filter(Q(nivel__gte=10) | Q(name__startswith="Admin"))

    para ver la query que se esta ejecutando:
    str(Character.objects.filter(Q(nivel__gte=10) | Q(name__startswith="Admin")).query)
    
    Para ver si existe alguno:
    Character.objects.filter(Q(nivel__gte=10) | Q(name__startswith="Admin")).exists()
    
"""
