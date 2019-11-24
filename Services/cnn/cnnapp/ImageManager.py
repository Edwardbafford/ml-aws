import os
from google.cloud import storage
from .containers.serviceContainer import Container


class GCPImageManager:
    def __init__(self):
        self.local_name = None
        self.blob = None
        self.c = Container()

    def download_image(self, image_name):
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(self.c.image_bucket)
        blob = bucket.blob(image_name + '.jpg')
        blob.download_to_filename(self.c.image_dir + blob.name)
        self.blob = blob
        self.local_name = blob.name

    def delete_local_image(self):
        try:
            os.remove(self.c.image_dir + self.local_name)
        except:
            # TODO - log
            print('Local image does not exist')

    def delete_remote_image(self):
        try:
            self.blob.delete()
        except:
            # TODO - log
            print('Remote image does not exist')
