from .serializers import ProductSerializer
from django.shortcuts import render
from rest_framework import generics
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins, permissions, authentication
from .permissions import IsStuffEditorPermission
from api.authentication import TokenAuthentication

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
    permission_classes = [IsStuffEditorPermission,permissions.IsAdminUser] 
    authentication_classes = [TokenAuthentication ,authentication.SessionAuthentication]
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
    permission_classes = []
    authentication_classes = []


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
            content = title

        serializer.save(content=content)
        return Response(serializer.data)


class ProductMixinView(
        generics.GenericAPIView,
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"  #default

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.update(request, *args, **kwargs)
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # serializer.save (user = self.request.user)
        content = serializer.validated_data.get("content") or None
        if not content:
            title = serializer.validated_data.get("title")
            content = title
        serializer.save(content=content)

    def perform_update(self, serializer):
        serializer.save()


product_mixin_view = ProductMixinView.as_view()