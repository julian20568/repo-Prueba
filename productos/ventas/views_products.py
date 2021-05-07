#from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from ventas.models import Products
from ventas.serializers import ProductsSerializer
from rest_framework.decorators import api_view
from rest_framework import status
#from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
#########################
##METODOS PARA PRODUCTS##
#########################

#Consultar products
@api_view(['GET', 'POST'])
def MetProducts(request):

    if request.method == 'GET':
        Pro=Products.objects.all()
        serializer=ProductsSerializer(Pro,many=True)
        return JsonResponse(serializer.data,safe=False)

#Guardar products
    elif request.method == 'POST':  
        serializer = ProductsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#busqueda de products
@api_view(['GET', 'PUT', 'DELETE'])
def products_detail(request,key):
    try:
        pro = Products.objects.get(pk=key)
    except Products.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductsSerializer(pro)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductsSerializer(pro, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pro.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#consulta de bills por name
@api_view(['GET'])
def products_name(request,nom):
    try:
        pro = Products.objects.get(name=nom)
    except Products.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductsSerializer(pro)
        return JsonResponse(serializer.data)

#consulta de bills por precio
@api_view(['GET'])
def products_precio(request,pre):
    try:
        pro = Products.objects.get(precio=pre)
    except Products.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductsSerializer(pro)
        return JsonResponse(serializer.data)
