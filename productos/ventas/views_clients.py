#from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from ventas.models import Clients
from ventas.serializers import ClientsSerializer
from rest_framework.decorators import api_view
from rest_framework import status
#from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
############################
##METODOS PARA LOS CLIENTS##
############################

#Consultar clients
@api_view(['GET', 'POST'])
def MetClients(request):

    if request.method == 'GET':
        Cli=Clients.objects.all()
        serializer=ClientsSerializer(Cli,many=True)
        return JsonResponse(serializer.data,safe=False)
    
#Guardar clients
    elif request.method == 'POST':  
        serializer = ClientsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#busqueda clients
@api_view(['GET', 'PUT', 'DELETE'])
def clients_detail(request,key):
    try:
        clients = Clients.objects.get(pk=key)
    except Clients.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientsSerializer(clients)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClientsSerializer(clients, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        clients.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#consulta de clients por firts_name
@api_view(['GET'])
def Clients_nombre(request,nom):
    try:
        clients = Clients.objects.get(firts_name=nom)
    except Clients.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientsSerializer(clients)
        return JsonResponse(serializer.data)

#consulta de clients por last_name
@api_view(['GET'])
def Clients_apellido(request,ape):
    try:
        clients = Clients.objects.get(last_name=ape)
    except Clients.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientsSerializer(clients)
        return JsonResponse(serializer.data)