from django.db import models

# Create your models here.

class compras(models.Model):
    compra = models.CharField(max_length=64)
    preço = models.CharField(max_length=64)
    
