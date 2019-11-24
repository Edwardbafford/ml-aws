import os
from django.apps import AppConfig
from google.cloud import storage
from .containers.mainContainer import Container
c = Container()

# cnnapp configuration
# downloads CNN model at startup

class CnnappConfig(AppConfig):
    name = 'cnnapp'
    
    def ready(self):

        try:
            if os.environ['ML_AWS_ENV'] == 'DEV':
                # TODO - logging
                print('skipping model download in ')
                return
            else:
                # TODO - logging
                print('downloading model')
        except KeyError as error:
            # TODO - logging
            print('downloading model')

        c.download_model()
