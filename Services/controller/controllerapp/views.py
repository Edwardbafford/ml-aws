from django.shortcuts import render
from .services import store_image, cnn_prediction
from PIL import Image
from resizeimage import resizeimage

def index(request):
    return render(request,'index.html')

def flower(request):
    if request.method == 'POST':
        myfile = request.FILES['filename']

        #TODO - env var?
        filename = './controllerapp/static/' + myfile.name
	    
        with open(filename, 'wb') as destination:
            for chunk in myfile.chunks():
                destination.write(chunk)

        store_image(filename, myfile.name)

        img_file = open(filename, 'rb')
        img = Image.open(img_file)
        img = resizeimage.resize_width(img, 200)
        img.save(filename, img.format)
        img_file.close()

        results = cnn_prediction(myfile.name)
        results['filename'] = myfile.name
        return render(request, 'file-upload.html',results)
    else:
        return render(request,'file-upload.html')