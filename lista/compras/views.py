
from django.shortcuts import render
from .models import compras

# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": compras.objects.all()
    })