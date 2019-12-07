import uuid
from PIL import Image
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
        filename = container.base_file + rand_name

        # write file locally
        with open(filename, 'wb') as destination:
            for chunk in request.FILES['filename'].chunks():
                destination.write(chunk)

        # check file validity
        try:
            img = Image.open(filename)
            img.verify()
        except (IOError, SyntaxError) as e:
            # TODO - log
            print('corrupt file')
            Thread(target=container.clean_image, args=(filename,)).start()
            return render(request, container.cnn_view, {'corrupt': True})

        # resize local image for browser view
        resize = Thread(target=container.resize_image, args=(filename,))
        resize.start()

        # get prediction data
        try:
            container.store_image(filename, rand_name)
            results = container.cnn_prediction(rand_name)
        except Exception as e:
            # TODO - log
            print('processing error')
            return render(request, container.cnn_view, {'error': True})

        # create view
        resize.join()
        results['filename'] = rand_name
        view = render(request, container.cnn_view, results)
        
        # delete local image in background
        Thread(target=container.clean_image, args=(filename,)).start()
        
        return view
    else:
        # Base view
        return render(request, container.cnn_view)
