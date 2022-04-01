from django.shortcuts import render
from .models import Nombre
from django.views.generic import ListView

# Create your views here.


class NombreListView(ListView):
    model = Nombre
    template_name = "index.html"
