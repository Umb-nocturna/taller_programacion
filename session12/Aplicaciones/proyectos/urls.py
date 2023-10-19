from django.urls import path
from . import views

urlpatterns = [ 
    path("proyectos/", views.proyectos, name="Proyectos"),
]