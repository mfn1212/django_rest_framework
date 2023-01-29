from django.contrib import admin
from django.urls import include, path
from .views import  product_list_view, product_create_view, product_destroy_view, product_detail_view, product_listcreat_view, product_update_view

urlpatterns = [
    path('list/', product_list_view),
    path('listcreate/', product_listcreat_view),
    path('<int:pk>/', product_detail_view),
    path('create/', product_create_view),
    path('update/<int:pk>/', product_update_view),
    path('destroy/<int:pk>/', product_destroy_view),

]
