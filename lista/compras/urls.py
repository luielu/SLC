from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("<int:compras_id>", views.compras, name="compras"),
   

]