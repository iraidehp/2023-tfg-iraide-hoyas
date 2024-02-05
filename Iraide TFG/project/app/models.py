from django.db import models

# Create your models here.
class usuario(models.Model):
    user =models.CharField(max_length=10, null=True)
    pwd= models.CharField(max_length=10, null=True)
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    pais = models.CharField(max_length=20)
    sexo = models.CharField(max_length=20)
    so = models.CharField(max_length=20)
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class clase(models.Model):
    nombre = models.CharField(max_length=20)
    usuarios = models.ManyToManyField(usuario)

