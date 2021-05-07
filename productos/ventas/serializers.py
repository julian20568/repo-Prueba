from rest_framework import serializers
from ventas.models import Clients
from ventas.models import Bills
from ventas.models import Products
from ventas.models import BillsProducts

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Clients
        fields=['id','document','firts_name','last_name','email']

class BillsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bills
        fields=['id','company_name','nit','code','client_id']

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['id','name','description','precio']

class BillsProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=BillsProducts
        fields=['id','bill_id','product_id']