from django.db import models

# Create your models here.

class Lista(models.Model):
    nome = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nome}"



class Compras(models.Model):
    compra = models.CharField(max_length=64)
    preco = models.IntegerField()
    
    def __str__(self):
        return f"ID:{self.id} Preço:{self.preco}  Produto:{self.compra}"



class Marcas(models.Model):
    marca = models.CharField(max_length=64)
    compras = models.ManyToManyField(Compras, blank=True, related_name="marcas")

    def __str__(self):
        return f"ID:{self.id} {self.marca} {self.compras}"
