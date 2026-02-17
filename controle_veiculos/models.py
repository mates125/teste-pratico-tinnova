from django.db import models

# Create your models here.

class VeiculoManager(models.Manager):
    def ativos(self):
        return self.filter(ativo=True)
    
    def filtrar(self, marca=None, ano=None, cor=None, min_preco=None, max_preco=None):
        qs = self.ativos()

        if marca:
            qs = qs.filter(marca=marca)
        if ano:
            qs = qs.filter(ano=ano)
        if cor:
            qs = qs.filter(cor=cor)
        if min_preco:
            qs = qs.filter(preco_usd__gte=min_preco)
        if max_preco:
            qs = qs.filter(preco_usd__lte=max_preco)
            
        return qs
    
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