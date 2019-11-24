from ..ImageManager import GCPImageManager
from ..services import google_model_make_prediction, google_download_model


# Abstraction layer for non-service files
class Container():
    def __init__(self):
        #Functions
        self.make_prediction = google_model_make_prediction
        self.download_model = google_download_model
        #Classes
        self.im = GCPImageManager()
