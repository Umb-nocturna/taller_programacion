from django.shortcuts import render
from .models import Proyecto

# Create your views here.
def proyectos(request):
    mis_proyectos = Proyecto.objects.all()
    return render(request,"pages/proyectos.html",{"proyectos":mis_proyectos})