from django.urls import path
from . import views

urlpatterns = [ 
    path("contacto/", views.contacto, name="Contacto"),
]