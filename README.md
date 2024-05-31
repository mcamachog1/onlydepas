# Extensión de User de Django usando One-to-One Profile Model
## 1. En views.py definir el Modelo
```

class Profile(models.Model):
    USUARIO = "U"
    ADMINISTRADOR = "A"
    TIPO_USUARIO_CHOICES = [(USUARIO,"Usuario"),(ADMINISTRADOR, "Administrador")]
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, default="USUARIO",choices=TIPO_USUARIO_CHOICES)
```