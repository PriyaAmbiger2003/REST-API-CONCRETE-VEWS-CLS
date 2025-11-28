from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import (CreateAPIView,ListAPIView,UpdateAPIView,
DestroyAPIView,RetrieveAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView)

# Create your views here.
class ListCreateProductView(ListAPIView,CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# class RetrieveupdatedestroyProductView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class RetrieveupdatedestroyProductView(ListCreateAPIView,RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer