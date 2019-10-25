from django.apps import AppConfig
from google.cloud import storage

class CnnappConfig(AppConfig):
    name = 'cnnapp'
    
    def ready(self):        
        storage_client = storage.Client()

        blobs = storage_client.list_blobs('cnn-model')
        bucket = storage_client.get_bucket('cnn-model')

        for blob in blobs:
            blob = bucket.blob(blob.name)
            blob.download_to_filename("./cnnapp/model/" + blob.name)
