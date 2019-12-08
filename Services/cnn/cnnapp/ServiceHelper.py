import os
import logging
import numpy as np
from PIL import Image
from skimage.transform import resize
from .exceptions import ImageCorrupt
logging.basicConfig(filename='{0}/cnn-app.log'.format(os.environ['LOG_LOCATION']),
                    format='%(asctime)s - %(levelname)s - %(message)s')
# Functions only to be used in service layer


# verify image is in proper jpg format
def verify_image(image):
    try:
        img = Image.open(image)
        img.verify()
    except (IOError, SyntaxError) as e:
        message = '{0} is bad or corrupted'.format(image.split('/')[-1])
        logging.error(message)
        raise ImageCorrupt(message)
    return


# scales image for processing by CNN
def prepare_image(image, target_width, target_height, max_zoom):
    height = image.shape[0]
    width = image.shape[1]
    image_ratio = width / height
    target_image_ratio = target_width / target_height
    crop_vertically = image_ratio < target_image_ratio
    crop_width = width if crop_vertically else int(height * target_image_ratio)
    crop_height = int(width / target_image_ratio) if crop_vertically else height
    resize_factor = np.random.rand() * max_zoom + 1.0
    crop_width = int(crop_width / resize_factor)
    crop_height = int(crop_height / resize_factor)
    x0 = np.random.randint(0, width - crop_width)
    y0 = np.random.randint(0, height - crop_height)
    x1 = x0 + crop_width
    y1 = y0 + crop_height
    return resize(image[y0:y1, x0:x1], (target_width, target_height)).astype(np.float32)
