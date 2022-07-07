from rest_framework import serializers
from ESB_api.models import *

class Cliente_serializer(serializers.HyperlinkedModelSerializer):
    facturas = serializers.StringRelatedField(many=True)
    class Meta:
        model = Cliente
        fields = ['cedula', 'nombre', 'apellido', 'telefono', 'correo', 'facturas']

class Producto_serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Producto
        fields = ['nombre_producto', 'tipo', 'precio']

class Tienda_serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tienda
        fields = ['ciudad', 'telefono']

class Factura_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Factura
        fields = ['fecha_hora', 'id_producto', 'id_cliente', 'id_tienda']
        
class json_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = json_prueba
        fields = ['json_field']