#from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from ventas.models import BillsProducts
from ventas.serializers import BillsProductsSerializer
from rest_framework.decorators import api_view
from rest_framework import status
#from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
#########################
##METODOS PARA BILLSPRODUCTS##
#########################

#Consultar billsproducts
@api_view(['GET', 'POST'])
def MetBillsProducts(request):

    if request.method == 'GET':
        BillPro=BillsProducts.objects.all()
        serializer=BillsProductsSerializer(BillPro,many=True)
        return JsonResponse(serializer.data,safe=False)

#Guardar billsproducts
    elif request.method == 'POST':  
        serializer = BillsProductsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#busqueda de billsproducts
@api_view(['GET', 'PUT', 'DELETE'])
def billsproducts_detail(request,key):
    try:
        BillPro = BillsProducts.objects.get(pk=key)
    except BillsProducts.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BillsProductsSerializer(BillPro)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BillsProductsSerializer(BillPro, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        BillPro.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
