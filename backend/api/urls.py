from django.urls import path,include
from . views import api_home
urlpatterns = [
    path('home/',api_home),
    path('product/',include('products.urls')),
]