import os
import google
import logging
from google.cloud import storage
from .exceptions import ImageNotFound
from .containers.serviceContainer import Container
logging.basicConfig(filename='{0}/cnn-app.log'.format(os.environ['LOG_LOCATION']),
                    format='%(asctime)s - %(levelname)s - %(message)s')
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
            message = '{0} was not found on GCP'.format(image_name + '.jpg')
            logging.error(message)
            raise ImageNotFound(message)

    def delete_local_image(self):
        try:
            os.remove(self.c.image_dir + self.local_name)
        except FileNotFoundError:
            logging.warning('Local {0} does not exist'.format(self.local_name))

    def delete_remote_image(self):
        try:
            self.blob.delete()
        except google.api_core.exceptions.NotFound:
            logging.warning('Remote {0} does not exist'.format(self.local_name))
