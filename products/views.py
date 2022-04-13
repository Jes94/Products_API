from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductsSerializer
from rest_framework import status
from .models import Products
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET', 'POST'])
def products_list(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def product_details(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'GET':
        serializer = ProductsSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductsSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)