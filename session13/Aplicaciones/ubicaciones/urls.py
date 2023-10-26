from django.urls import path
from . import views

urlpatterns = [ 
    path("sitios/", views.sitios_interes, name="Sitios"),
]


#https://www.latlong.net/convert-address-to-lat-long.html