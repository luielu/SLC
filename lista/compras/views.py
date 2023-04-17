
from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Compras, Marcas

# Create your views here.

def index(request):
    return render(request, "compras/index.html", {
        "compras": Compras.objects.all()
    })

def compras(request, compras_id):
    compra = Compras.objects.get(id=compras_id)
    marcas = compra.marcas.all()
  
    return render(request, "compras/pag.html", {
        "compras": compra,
        "marcas": marcas,
      
    })
 