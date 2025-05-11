from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify # Importa slugify para generar slugs amigables

class Estudiante(models.Model):
    nombre = models.CharField(blank=False, max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    slug = models.SlugField(unique=True, blank=True, max_length=200) 

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profesion = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, max_length=200) 


    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.profesion}"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField(unique=True)

    def __str__(self):
        return self.nombre

class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return self.nombre