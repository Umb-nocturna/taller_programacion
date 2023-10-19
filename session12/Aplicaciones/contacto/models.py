from django.db import models

# Create your models here.
class Contacto(models.Model):
    date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    phone = models.CharField(max_length=90)
    message = models.CharField( max_length=2000 )
    