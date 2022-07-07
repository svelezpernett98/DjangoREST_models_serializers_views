from os import stat
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import action
from ESB_api.models import *
from ESB_api.serializers import *
from ESB_api.forms import formulario_json


# Create your views here.

class Cliente_viewset(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = Cliente_serializer

    #@action(methods=['get'], detail=True, url_path='get', url_name='change_password')
    def get(self, request):
        self.serializer_class(self.queryset, many=True)
        return Response(self.serializer_class.data)

    def post(self, request, format=None):
        serialized_data_POST = self.serializer_class(data=request.data)
        if serialized_data_POST.is_valid():
            serialized_data_POST.save()
            return Response(serialized_data_POST.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data_POST.errors, status=status.HTTP_400_BAD_REQUEST)

class Producto_viewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = Producto_serializer

    #@action(methods=['get'], detail=True, url_path='get', url_name='change_password')
    def get(self, request):
        self.serializer_class(self.queryset, many=True)
        return Response(self.serializer_class.data)

    def post(self, request, format=None):
        serialized_data_POST = self.serializer_class(data=request.data)
        if serialized_data_POST.is_valid():
            serialized_data_POST.save()
            return Response(serialized_data_POST.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data_POST.errors, status=status.HTTP_400_BAD_REQUEST)

class Tienda_viewset(viewsets.ModelViewSet):
    queryset = Tienda.objects.all()
    serializer_class = Tienda_serializer

    #@action(methods=['get'], detail=True, url_path='get', url_name='change_password')
    def get(self, request):
        self.serializer_class(self.queryset, many=True)
        return Response(self.serializer_class.data)

    def post(self, request, format=None):
        serialized_data_POST = self.serializer_class(data=request.data)
        if serialized_data_POST.is_valid():
            serialized_data_POST.save()
            return Response(serialized_data_POST.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data_POST.errors, status=status.HTTP_400_BAD_REQUEST)

class Factura_viewset(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = Factura_serializer

    #@action(methods=['get'], detail=True, url_path='get', url_name='change_password')
    def get(self, request):
        self.serializer_class(self.queryset, many=True)
        return Response(self.serializer_class.data)

    def post(self, request, format=None):
        serialized_data_POST = self.serializer_class(data=request.data)
        if serialized_data_POST.is_valid():
            serialized_data_POST.save()
            return Response(serialized_data_POST.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data_POST.errors, status=status.HTTP_400_BAD_REQUEST)

class json_viewset(viewsets.ModelViewSet):
    queryset = json_prueba.objects.all()
    serializer_class = json_serializer
    
    def get(self, request):
        self.serializer_class(self.queryset, many=True)
        return Response(self.serializer_class.data)
    
    def post(self, request, format=None):
        
        # if request.method=="POST":
        #     obj_formulario_json = formulario_json(request.POST)
            
        #     if obj_formulario_json.is_valid():
        #         json_form = obj_formulario_json.cleaned_data  
                serialized_data_POST = self.serializer_class(data=json_form)
                if serialized_data_POST.is_valid():
                    serialized_data_POST.save()
                    return Response(serialized_data_POST.data, status=status.HTTP_201_CREATED)
                return Response(serialized_data_POST.errors, status=status.HTTP_400_BAD_REQUEST)
        
