from django.shortcuts import render
from .serializers import ProductsSerializer
from rest_framework import generics
from .models import Products
from rest_framework import viewsets
from rest_framework.response import Response

class ProductsAPIView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

def get_invoice():
    # Реализация вашей функции
    return "Результат выполнения функции"

class InvoiceViewSet(viewsets.ViewSet):
    def list(self, request):
        result = get_invoice()
        return Response({"result": result})
