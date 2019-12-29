

# Abstraction layer for service files
class Container():
    def __init__(self):
        # Literals
        self.image_bucket = 'cnn-images'
        self.cnn_host = 'CNNSVC_SERVICE_HOST'
        self.cnn_port = 'CNNSVC_SERVICE_PORT'
        self.cnn_url = 'prediction'
        self.file_width = 400
