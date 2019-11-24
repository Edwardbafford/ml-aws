

# Abstraction layer for service files
class Container():
    def __init__(self):
        self.image_bucket = 'cnn-images'
        self.model_bucket = 'cnn-model'
        self.image_dir = "./cnnapp/images/"
        self.model_dir = "./cnnapp/model/"
        self.model_name = 'flower_classifier.ckpt'
