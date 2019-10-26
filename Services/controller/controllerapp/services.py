import os
import time
import requests
from google.cloud import storage

def store_image(load,save):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('cnn-images')
    blob = bucket.blob(save)
    blob.upload_from_filename(load)
    return

def clean_images(filename):
    time.sleep(2)
    os.remove(filename)
    return

def cnn_prediction(filename):
    #TODO - Make call to microservice and get predictions
    cleaned_name = '.'.join(filename.split('.')[:-1])
    URL = 'http://{0}:{1}/prediction/{2}'.format(
            os.environ['CNNSVC_SERVICE_HOST'],
            os.environ['CNNSVC_SERVICE_PORT'],
            cleaned_name)
    probs = requests.get(url = URL).json()["preds"]
    
    return dict(zip(['Daisy','Dandelion','Rose','Sunflower','Tulip'], probs))

