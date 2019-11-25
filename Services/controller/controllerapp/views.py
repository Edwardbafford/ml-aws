import uuid
from threading import Thread
from django.shortcuts import render
from .containers.viewContainer import Container
container = Container()

# Handles incoming HTTP requests


# Home page
def index(request):
    return render(request, container.home_view)


# CNN view
def flower(request):
    # Uploading a file
    if request.method == 'POST':
        rand_name = str(uuid.uuid4()) + '.jpg'

        # write file locally
        filename = container.base_file + rand_name
        with open(filename, 'wb') as destination:
            for chunk in request.FILES['filename'].chunks():
                destination.write(chunk)

        # resize local image for browser view
        resize = Thread(target=container.resize_image, args=(filename,))
        resize.start()

        # get prediction data
        container.store_image(filename, rand_name)
        results = container.cnn_prediction(rand_name)
        results['filename'] = rand_name
        resize.join()
        view = render(request, container.cnn_view, results)
        
        # Delete local image in background
        clean = Thread(target=container.clean_image, args=(filename,))
        clean.start()
        
        return view
    else:
        # Base view
        return render(request, container.cnn_view)
