from .serializers import ProductSerializer
from django.shortcuts import render
from rest_framework import generics
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductDetailAPIView.as_view()


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_list_view = ProductListAPIView.as_view()


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)     # diffrent work in serializer depond on user
        content = serializer.validated_data.get("content") or None
        if not content:
            title = serializer.validated_data.get("title")
            content = title
        serializer.save(content=content)


product_listcreat_view = ProductListCreateAPIView.as_view()


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)     # diffrent work in serializer depond on user
        content = serializer.validated_data.get("content") or None
        if not content:
            title = serializer.validated_data.get("title")
            content = title
        serializer.save(content=content)


product_create_view = ProductCreateAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        # send_email_confirmation(user=self.request.user, modified=instance)


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_destroy_view = ProductDestroyAPIView.as_view()

@api_view(["POST", "GET"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk:
            instace = Product.objects.get(pk=pk)
            data = ProductSerializer(instance=instace, many=False).data
        else:
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
        return Response(data)
    
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        content = serializer.validated_data.get("content") or None
        if not content:
            title = serializer.validated_data.get("title")
            content =title
        
        serializer.save(content=content)
        return Response(serializer.data)