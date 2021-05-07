from django.db import models

# Create your models here.

class Clients(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.CharField(max_length=100, blank=False, null=False)
    firts_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField()

class Bills(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100, blank=False, null=False)
    nit = models.IntegerField(blank=False, null=False)
    code = models.IntegerField(blank=False, null=False)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE, null=False)
   
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    precio = models.CharField(max_length=100, blank=False, null=False)

class BillsProducts(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bills, on_delete=models.CASCADE, null=False)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, null=False)