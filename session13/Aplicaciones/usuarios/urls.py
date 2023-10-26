from django.urls import path
from . import views

urlpatterns = [ 
    path('exit/', views.exit, name="exit"),
    
]
