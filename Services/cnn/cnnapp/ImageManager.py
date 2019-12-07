import os
import google
from google.cloud import storage
from .exceptions import ImageNotFound
from .containers.serviceContainer import Container
# Image manager implementations


# GCPImageManager - manages from a remote GCP Storage bucket
class GCPImageManager:
    def __init__(self):
        self.local_name = None
        self.blob = None
        self.c = Container()

    def download_image(self, image_name):
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(self.c.image_bucket)
        blob = bucket.blob(image_name + '.jpg')
        self.blob = blob
        self.local_name = blob.name
        # raise exception if file doesnt exist in GCP
        try:
            blob.download_to_filename(self.c.image_dir + blob.name)
        except google.api_core.exceptions.NotFound as ex:
            # TODO - log
            message = 'Image {0}/{1} was not found on GCP'.format(self.c.image_bucket,image_name + '.jpg')
            print(message)
            raise ImageNotFound(message)

    def delete_local_image(self):
        try:
            os.remove(self.c.image_dir + self.local_name)
        except FileNotFoundError:
            # TODO - log
            print('Local image does not exist')

    def delete_remote_image(self):
        try:
            self.blob.delete()
        except google.api_core.exceptions.NotFound:
            # TODO - log
            print('Remote image does not exist')
