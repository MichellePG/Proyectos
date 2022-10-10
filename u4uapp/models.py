from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Universidad(models.Model):
    nombre=models.CharField(max_length=128)
    tipo=models.CharField(max_length=128)
    comuna=models.CharField(max_length=128)
    region=models.CharField(max_length=128)
    estudiantes=models.IntegerField()
    fundacion=models.IntegerField()

class Carrera(models.Model):
    nombre=models.CharField(max_length=128)
    universidades=models.ManyToManyField(Universidad)
    infog= models.CharField(max_length=256) 

class Comentario(models.Model):
    contenido=models.TextField()
    fecha_creacion=models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    universidad=models.ForeignKey(Universidad, on_delete=models.CASCADE)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)

class Carreraesp(models.Model):
    nombrec=models.TextField(max_length=256)
    area=models.TextField(max_length=256)
    puntaje=models.CharField(max_length=256)
    porcentaje=models.CharField(max_length=256)
    duracion=models.CharField(max_length=256)
    ubicacion=models.CharField(max_length=256)
