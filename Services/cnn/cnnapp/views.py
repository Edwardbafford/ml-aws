from django.http import JsonResponse
from .containers.mainContainer import Container
c = Container()

# Handle incoming requests


# Testing url
def index_test(request):
    return JsonResponse({'test_successful': 'True'})


# Makes prediction based on name of file given in URL
def prediction(request, image):
    c.im.download_image(image)
    preds = c.make_prediction(c.im.local_name)
    c.im.delete_remote_image()
    c.im.delete_local_image()
    return JsonResponse({'preds': preds})
