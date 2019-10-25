import _thread
from PIL import Image
from django.shortcuts import render
from resizeimage import resizeimage
from .services import store_image, cnn_prediction, clean_images

def index(request):
    return render(request,'index.html')

#TODO - multithreading
#TODO - extract dependencies
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
        
        try:
            img = resizeimage.resize_width(img, 200)
        except:
            print('small image')
        
        img.save(filename, img.format)
        img_file.close()

        results = cnn_prediction(myfile.name)
        results['filename'] = myfile.name
        view = render(request, 'file-upload.html',results)
        
        _thread.start_new_thread(clean_images,(filename,))
        
        return view
    else:
        return render(request,'file-upload.html')