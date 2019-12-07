# Custom Exceptions


# Image not found when asked to make a prediction
class ImageNotFound(Exception):
    pass


# Image is not in proper jpg format
class ImageCorrupt(Exception):
    pass
