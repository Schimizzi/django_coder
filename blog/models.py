from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField(max_length=500)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} /n {self.contenido} /n {self.fecha_publicacion}"
