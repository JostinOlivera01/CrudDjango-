from distutils.command.upload import upload
from operator import truediv
from pickle import TRUE
from django.db import models

# Create your models here.

class Libro(models.Model):
    id= models.AutoField(primary_key=TRUE)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Imagen')
    description = models.TextField(null=TRUE, verbose_name='Descripcion')
    
    def __str__(self):
        fila = " TITULO: " + self.titulo + " - " + " DESCRIPCION: " + self.description
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class Cliente(models.Model):
    id= models.AutoField(primary_key=TRUE) 
     