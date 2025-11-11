from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    telefono = models.IntegerField(unique=True)
    dui = models.CharField(max_length=10, unique=True)
    

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

# Create your models here.
