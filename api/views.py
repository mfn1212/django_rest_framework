from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product


def api_home(request, *args, **kwargs):
    # json_data = {
    #     'massage': "hi here is my first api"
    # }
    # return JsonResponse(json_data)
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['title'] = model_data.title 
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)    