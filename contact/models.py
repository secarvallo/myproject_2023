from django.db import models

# Create your models here.
class Contact(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    celular = models.IntegerField()
    comentario = models.TextField(max_length=100)

    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.nombre, self.email) 