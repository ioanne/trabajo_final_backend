from django.db import models

"""Empleado
id, nommbre, apellido, dni, fk_domicilio

Cliente
id, nommbre, apellido, dni, fk_domicilio

compra
id, fk_domicilio, id_empleado(vendedor), fk_cliente

detalle_compra
id, cantidad, fk_compra, fk_producto

inventario
id, fk_producto, cantidad

producto
id, nombre

domicilio
id, fk_localidad

localidad
id, fk_ciudad

ciudad
id, fk_provincia

provincia
id, fk_pais

pais
id
"""


""" 
En django podemos crear clases con 
    class Meta:
        abstract = True

Esto indica que esa clase no va a crear una tabla,
unicamente va a tener informacion que se va a heredar a otras clases y esas pueden tener
nuevamente el abstract = True, de lo contrario, ahi se crea la tabla.
"""
from django.contrib.auth.models import User


class ModeloPersonalizado(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    created_by_user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name="%(class)s_created_by_user",
    )

    updated_datetime = models.DateTimeField(auto_now=True)
    updated_by_user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name="%(class)s_updated_by_user",
    )

    deleted_datetime = models.DateTimeField(blank=True, null=True)
    deleted_by_user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        db_index=True,
        related_name="%(class)s_deleted_by_user",
    )

    class Meta:
        abstract = True


class Persona(ModeloPersonalizado):  # Modelos abstractas
    """
    Persona no existe en la base de datos.

    Se crea una tabla empleados con:
    id, nombre, apellido, dni, fk_domicilio

    Se crea una tabla cliente con:
    id, nombre, apellido, dni, fk_domicilio
    """

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Empleado(Persona):  # Tabla
    domicilio = models.ForeignKey(
        "Domicilio", on_delete=models.CASCADE, related_name="empleados"
    )


class Cliente(Persona):  # Tabla
    domicilio = models.ForeignKey(
        "Domicilio", on_delete=models.CASCADE, related_name="clientes"
    )


class Producto(ModeloPersonalizado):  # Tabla
    nombre = models.CharField(max_length=50)


class Compra(ModeloPersonalizado):  # Tabla
    domicilio = models.ForeignKey(
        "Domicilio", on_delete=models.CASCADE, related_name="compras"
    )
    vendedor = models.ForeignKey(
        "Empleado", on_delete=models.CASCADE, related_name="compras"
    )
    cliente = models.ForeignKey(
        "Cliente", on_delete=models.CASCADE, related_name="compras"
    )


class Detalle(ModeloPersonalizado):
    cantidad = models.PositiveIntegerField()
    compra = models.ForeignKey(
        "Compra", on_delete=models.CASCADE, related_name="detalles"
    )
    producto = models.ForeignKey(
        "Producto", on_delete=models.CASCADE, related_name="detalles"
    )


class Inventario(ModeloPersonalizado):
    cantidad = models.PositiveIntegerField()
    producto = models.ForeignKey(
        "Producto", on_delete=models.CASCADE, related_name="inventarios"
    )


class Domicilio(ModeloPersonalizado):  # Tabla
    calle = models.CharField(max_length=50)
    numero = models.PositiveIntegerField()
    localidad = models.ForeignKey(
        "Localidad", on_delete=models.CASCADE, related_name="domicilios"
    )


class Localidad(ModeloPersonalizado):
    nombre = models.CharField(max_length=50)
    ciudad = models.ForeignKey(
        "Ciudad", on_delete=models.CASCADE, related_name="localidades"
    )


class Ciudad(ModeloPersonalizado):
    nombre = models.CharField(max_length=50)
    provincia = models.ForeignKey(
        "Provincia", on_delete=models.CASCADE, related_name="ciudades"
    )


class Provincia(ModeloPersonalizado):
    nombre = models.CharField(max_length=50)
    pais = models.ForeignKey(
        "Pais", on_delete=models.CASCADE, related_name="provincias"
    )


class Pais(ModeloPersonalizado):
    nombre = models.CharField(max_length=50)
