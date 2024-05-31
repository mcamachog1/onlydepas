from django.conf import settings
from django.db import models




# Create your models here.
class Profile(models.Model):
    USUARIO = "U"
    ADMINISTRADOR = "A"
    TIPO_USUARIO_CHOICES = [(USUARIO,"Usuario"),(ADMINISTRADOR, "Administrador")]
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, default="USUARIO",choices=TIPO_USUARIO_CHOICES)

   
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150, null=True)


class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200)
    imagen = models.URLField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,related_name='productos')
    auditoria = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Auditoria')

class Auditoria(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='auditores')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,related_name='productos_auditados')
    detalles = models.TextField()
    fecha_hora = models.DateTimeField()
    aprobacion = models.BooleanField()

class Contacto(models.Model):
    nombre = models.CharField(max_length=60)
    email = models.EmailField()
    mensaje = models.TextField()