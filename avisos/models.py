from django.db import models
from django.conf import settings

# Create your models here.

class Assets(models.Model):
    ubicacion=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to="assets/%y")

    def __str__(self):
        return self.ubicacion
    

class User(models.Model):
    id_usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    ),
    avatar = models.ImageField()
    nick = models.CharField(max_length=100)


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(null=True, upload_to="img/%y")
    alt_text = models.CharField(null=True, max_length=100)
    descripcion = models.CharField(null=True, max_length=256)

    def __str__(self):
        return self.nombre

        
class Subcategoria(models.Model):
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(null=True)

 
    def __str__(self):
        return self.nombre


class Anuncio(models.Model):
    id_usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    ),
    visible = models.BooleanField(default=False)
    publicado = models.DateTimeField(auto_now=True, auto_now_add=True),
    caduca = models.DateTimeField(),
    id_categoria = models.ForeignKey(Categoria, default=-1, on_delete=models.SET_DEFAULT)
    id_subcategoria = models.ForeignKey(Subcategoria, default=-1, on_delete=models.SET_DEFAULT)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)

    def __str__(self):
        return self.titulo

    
class Imagen(models.Model):
    id_anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='img/anuncios/%y')
