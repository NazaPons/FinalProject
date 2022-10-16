from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    subtitulo = models.CharField(max_length=100, verbose_name='Sub Título')
    imagen = models.ImageField(upload_to='imagenes/', null = True, verbose_name='Imagen')
    contenido = models.TextField(verbose_name='Contenido', null = True)
    autor = models.CharField(max_length=50)
    fecha = models.DateField(null = True)

    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Subtitulo: " + self.subtitulo + " - " + "Autor: " + self.autor
        return fila

    def delete(self, using=None, keep_parent=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    #image

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

