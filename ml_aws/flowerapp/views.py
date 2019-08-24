import os
from django.shortcuts import render
from django.http import JsonResponse
from .services import make_prediction
from django.core.files.storage import FileSystemStorage

def index_test(request):
    return JsonResponse({'test_successful':'True'})

def flower(request):
    if request.method == 'POST':

        myfile = request.FILES['filename']
        with open('flowerapp/images/' + myfile.name, 'wb') as destination:
            for chunk in myfile.chunks():
                destination.write(chunk)
        
        probs = make_prediction(myfile.name)
        results = dict(zip(['Daisy','Dandelion','Rose','Sunflower','Tulip'], probs))
        
        os.remove('flowerapp/images/' + myfile.name)
        
        return render(request, 'flowerapp/file-upload.html',results)
    else:
        return render(request,'flowerapp/file-upload.html')