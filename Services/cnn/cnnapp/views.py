import os
from django.shortcuts import render
from django.http import JsonResponse
from .services import make_prediction
from django.core.files.storage import FileSystemStorage
from google.cloud import storage

def index_test(request):
    return JsonResponse({'test_successful':'True'})

def prediction(request, image):
    # Download image
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('cnn-images')
    blob = bucket.blob(image + '.jpg')
    blob.download_to_filename("./cnnapp/images/" + blob.name)
    
    # Make Prediction
    preds = make_prediction(blob.name)
    
    #Delete image from local and google cloud storage
    blob.delete()
    os.remove("./cnnapp/images/" + blob.name)
    
    return JsonResponse({'preds':preds})