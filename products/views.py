from .serializers import ProductSerializer
from django.shortcuts import render
from rest_framework import generics
from .models import Product


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductDetailAPIView.as_view()


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_list_view = ProductListAPIView.as_view()


class ProductListCreateAPIView (generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_listcreat_view = ProductListCreateAPIView.as_view()


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_create_view = ProductCreateAPIView.as_view()


class ProductUpdateAPIView  (generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView  (generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_destroy_view = ProductDestroyAPIView.as_view()
