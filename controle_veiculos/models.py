from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)