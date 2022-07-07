from django.urls import path, include
from rest_framework import routers
from ESB_api.views import *

router_api = routers.DefaultRouter()
router_api.register(r'clientes', Cliente_viewset)
router_api.register(r'productos', Producto_viewset)
router_api.register(r'tiendas', Tienda_viewset)
router_api.register(r'facturas', Factura_viewset)
router_api.register(r'json', json_viewset)
