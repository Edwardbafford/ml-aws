import os
from django.shortcuts import render
from django.http import JsonResponse
from .services import make_prediction
from django.core.files.storage import FileSystemStorage

def index_test(request):
    return JsonResponse({'test_successful':'True'})
