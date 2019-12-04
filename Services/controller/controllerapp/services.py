import os
import time
import requests
from PIL import Image
from resizeimage import resizeimage
from google.cloud import storage
from .containers.serviceContainer import Container
container = Container()

# Service layer functions to be used by views


# Upload file to GCP Storage bucket
def gcp_store_image(load, save):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(container.image_bucket)
    blob = bucket.blob(save)
    blob.upload_from_filename(load)
    return


# Make call to K8s micro service for CNN prediction
def k8s_cnn_prediction(filename):
    cleaned_name = '.'.join(filename.split('.')[:-1])
    URL = 'http://{0}:{1}/{2}/{3}'.format(
            os.environ[container.cnn_host],
            os.environ[container.cnn_port],
            container.cnn_url,
            cleaned_name)
    # TODO - log
    print(URL)
    probs = requests.get(url = URL).json()["preds"]
    return dict(zip(['Daisy','Dandelion','Rose','Sunflower','Tulip'], probs))


# Remove file from local system
def standard_clean_image(filename):
    time.sleep(5)
    os.remove(filename)
    return


# Resize the local image for view
def standard_resize_image(filename):
    img_file = open(filename, 'rb')
    img = Image.open(img_file)
    try:
        img = resizeimage.resize_width(img, container.file_width)
    except AttributeError:
        # TODO - log?
        print('small image')
    img.save(filename, img.format)
    img_file.close()
