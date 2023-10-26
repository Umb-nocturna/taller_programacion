from django.db import models

# Create your models here.
class Lugares(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre Sucursal')
    address = models.CharField(max_length=250, verbose_name='Dirección')
    lat = models.FloatField(verbose_name='Latitud')
    lng = models.FloatField(verbose_name='Longitud')

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
        ordering = ['name']

    def __str__(self):
        return self.name