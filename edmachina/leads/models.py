from django.db import models


class Materia(models.Model):

    nombre = models.CharField(max_length=100)


class Carrera(models.Model):

    nombre = models.CharField(max_length=100)
    materias = models.ManyToManyField(Materia)


class Lead(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    materias = models.ManyToManyField(Materia)
    carreras = models.ManyToManyField(Carrera)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)