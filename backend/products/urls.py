from django.contrib import admin
from django.urls import include, path
from .views import  product_alt_view, product_list_view, product_create_view, product_destroy_view, product_detail_view, product_listcreat_view, product_update_view,product_mixin_view

urlpatterns = [
    path('list/', product_list_view),
    path('listcreate/', product_listcreat_view),
    path('<int:pk>/', product_detail_view),
    path('create/', product_create_view),
    path('update/<int:pk>/', product_update_view),
    path('destroy/<int:pk>/', product_destroy_view),
    path('alt_view/<int:pk>/', product_alt_view),
    path('alt_view/', product_alt_view),
    path('mixin_view/', product_mixin_view),
    path('mixin_view/<int:pk>/', product_mixin_view),

]
