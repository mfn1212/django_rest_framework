from django.shortcuts import render
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    json_data = {
        'massage': "hi here is my first api"
    }
    return JsonResponse(json_data)

