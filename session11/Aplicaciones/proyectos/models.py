from django.db import models

# Create your models here.
class Proyecto(models.Model):
    date = models.DateTimeField(auto_now=True)
    codigo = models.CharField(primary_key=True,max_length=4)
    nombre = models.CharField(max_length=90)
    descripcion = models.CharField( max_length=2000 )
    imageproj = models.FileField(upload_to='proyectos/',null=True,)
    publish = models.BooleanField(default=True)
    
    def __str__(self):
        texto = "[{0}] {1}"
        if self.publish:
            t_publish = "On"
        else:
            t_publish = "Off"    
        return texto.format(t_publish, self.nombre)