from django.urls import path
from ventas import views_clients
from ventas import views_products
from ventas import views_bills
from ventas import views_billproducts

urlpatterns=[
    #############################
    #RUTAS PARA LA CLASE CLIENTS#
    #############################
    path('clients',views_clients.MetClients),
    path('clients/<int:key>',views_clients.clients_detail),
    path('clients/query/nombre/<str:nom>',views_clients.Clients_nombre),
    path('clients/query/apellido/<str:ape>',views_clients.Clients_apellido),

    ##################
    #RUTAS PARA BILLS#
    ##################
    path('bills',views_bills.MetBills),
    path('bills/<int:key>',views_bills.bills_detail),
    path('bills/query/nombre/<str:nom>',views_bills.Company_name),
    path('bills/query/nit/<str:nt>',views_bills.nit),

    #####################
    #RUTAS PARA PRODUCTS#
    #####################
    path('products',views_products.MetProducts),
    path('products/<int:key>',views_products.products_detail),
    path('products/query/nombre/<str:nom>',views_products.products_name),
    path('products/query/precio/<str:pre>',views_products.products_precio),

    ##########################
    #RUTAS PARA BILLSPRODUCTS#
    ##########################
    path('billsproducts',views_billproducts.MetBillsProducts),
    path('billsproducts/<int:key>',views_billproducts.billsproducts_detail),
]
