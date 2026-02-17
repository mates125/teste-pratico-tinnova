from django.db import models

# Create your models here.

class VeiculoManager(models.Manager):
    def ativos(self):
        return self.filter(ativo=True)
    
class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.CharField(max_length=50)
    preco_usd = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)

    objects = VeiculoManager()


class Usuario(models.Model):
    nome = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)