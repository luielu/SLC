
from django.shortcuts import render
from .models import compras, lista

# Create your views here.

def index(request):
    return render(request, "compras/index.html", {
        "compras": compras.objects.all()
    })

def compras(request, compras_id):
    compras = compras.objects.get(id=compras_id)
    return render(request, "compras/pag.html", {
        "compras": compras
    })
