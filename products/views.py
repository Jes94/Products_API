from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductsSerializer
from rest_framework import status
from .models import Products

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

@api_view(['GET'])
def product_details(request, pk):
    try:
        product = Products.objects.get(pk=pk)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)
    
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)