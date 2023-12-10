from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Oficina(models.Model):
    nombre = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    responsable = models.CharField(max_length=40, null=True)
    cp = models.CharField(max_length=5, default=0)
    
    def __str__(self):
        return "%s" % (self.nombre)
