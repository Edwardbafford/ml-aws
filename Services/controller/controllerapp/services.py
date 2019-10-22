import os
import time
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
    probs = [.2,.2,.2,.2,.2]
    return dict(zip(['Daisy','Dandelion','Rose','Sunflower','Tulip'], probs))

