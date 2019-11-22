import os
import time
import requests
from google.cloud import storage

from .containers.serviceContainer import Container
container = Container()

def gcp_store_image(load,save):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(container.image_bucket)
    blob = bucket.blob(save)
    blob.upload_from_filename(load)
    return

def k8s_cnn_prediction(filename):
    cleaned_name = '.'.join(filename.split('.')[:-1])
    URL = 'http://{0}:{1}/{2}/{3}'.format(
            os.environ[container.cnn_host],
            os.environ[container.cnn_port],
            container.cnn_url,
            cleaned_name)
    
    #TODO - log
    print(URL)
    
    probs = requests.get(url = URL).json()["preds"]
    
    return dict(zip(['Daisy','Dandelion','Rose','Sunflower','Tulip'], probs))

def standard_clean_image(filename):
    time.sleep(2)
    os.remove(filename)
    return