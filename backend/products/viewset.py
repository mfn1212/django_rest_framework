from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework import mixins


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # default


class ProductGenericViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # default
#you can use these views in your url patterns
product_detail_view = ProductGenericViewSet.as_view({'get':'retrieve'})
product_list_view = ProductGenericViewSet.as_view({'get':'list'})
