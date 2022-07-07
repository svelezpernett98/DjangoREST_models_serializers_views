from django.db import models
from rest_framework import serializers
from django.db import models

# Create your models here.

class Cliente(models.Model):
    cedula = models.CharField(primary_key=True, max_length=15, unique=True)
    nombre = models.CharField(max_length=30, blank=False, null=False)
    apellido = models.CharField(max_length=30, blank=False, null=False)
    telefono = models.CharField(max_length=15, blank=False, null=False)
    correo = models.EmailField(max_length=254, blank=False, null=False)
    
    
    def __str__(self):
        return self.nombre + ", CC " + self.cedula

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=30, blank=False, null=False)
    tipo = models.CharField(max_length=30, blank=False, null=False)
    precio = models.FloatField(max_length=8, blank=False, null=False)

    def __str__(self):
        return self.nombre_producto

class Tienda(models.Model):
    ciudad = models.CharField(max_length=30, blank=False, null=False)
    telefono = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return ("Maaji " + (self.ciudad))

class Factura(models.Model):
    fecha_hora = models.DateTimeField(auto_now=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, related_name='facturas', on_delete=models.CASCADE)
    id_tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['id_cliente', 'id']
        ordering = ['id']
    
    def __str__(self):
        return ("Factura #"+(str(self.id)+" "+(self.id_cliente.nombre)+" "+(self.id_cliente.apellido)+", CC: "+(self.id_cliente.cedula)))
    
class json_prueba(models.Model):
    json_field = models.JSONField(default=dict)
