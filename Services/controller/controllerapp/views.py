import _thread
from PIL import Image
from django.shortcuts import render
from resizeimage import resizeimage

from .containers.viewContainer import Container
container = Container()

def index(request):
    return render(request, container.home_view)


def flower(request):
    if request.method == 'POST':
        myfile = request.FILES['filename']

        filename = container.base_file + myfile.name
        
        with open(filename, 'wb') as destination:
            for chunk in myfile.chunks():
                destination.write(chunk)

        container.store_image(filename, myfile.name)

        img_file = open(filename, 'rb')
        img = Image.open(img_file)
        
        try:
            img = resizeimage.resize_width(img, container.file_width)
        except:
            #TODO - log?
            print('small image')
        
        img.save(filename, img.format)
        img_file.close()
        
        results = container.cnn_prediction(myfile.name)
        
        results['filename'] = myfile.name
        view = render(request, container.cnn_view, results)
        
        #Delete images in the background while view is returned
        _thread.start_new_thread(container.clean_image, (filename,))
        
        return view
    else:
        return render(request, container.cnn_view)