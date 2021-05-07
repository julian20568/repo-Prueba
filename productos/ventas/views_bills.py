#from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from ventas.models import Bills
from ventas.serializers import BillsSerializer
from rest_framework.decorators import api_view
from rest_framework import status
#from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
######################
##METODOS PARA BILLS##
######################

#Consultar bills
@api_view(['GET', 'POST'])
def MetBills(request):

    if request.method == 'GET':
        Bil=Bills.objects.all()
        serializer=BillsSerializer(Bil,many=True)
        return JsonResponse(serializer.data,safe=False)
    
#Guardar bils
    elif request.method == 'POST':  
        serializer = BillsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#busqueda de bills
@api_view(['GET', 'PUT', 'DELETE'])
def bills_detail(request,key):
    try:
        bills = Bills.objects.get(pk=key)
    except Bills.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BillsSerializer(bills)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BillsSerializer(bills, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bills.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#consulta de bills por company_name
@api_view(['GET'])
def Company_name(request,nom):
    try:
        bills = Bills.objects.get(company_name=nom)
    except Bills.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BillsSerializer(bills)
        return JsonResponse(serializer.data)

#consulta de bills por nit
@api_view(['GET'])
def nit(request,nt):
    try:
        bills = Bills.objects.get(nit=nt)
    except Bills.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BillsSerializer(bills)
        return JsonResponse(serializer.data)

#consulta de bills por code
@api_view(['GET'])
def code(request,cod):
    try:
        bills = Bills.objects.get(code=cod)
    except Bills.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BillsSerializer(bills)
        return JsonResponse(serializer.data)