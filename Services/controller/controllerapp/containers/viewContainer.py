# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 20:15:09 2019

@author: louie.bafford
"""

from ..services import gcp_store_image, k8s_cnn_prediction, standard_clean_image

class Container():
    def __init__(self):
        #Literals
        self.base_file = './controllerapp/static/'
        self.cnn_view = 'file-upload.html'
        self.home_view = 'index.html'
        self.file_width = 200    
        #Functions
        self.clean_image = standard_clean_image
        self.cnn_prediction = k8s_cnn_prediction
        self.store_image = gcp_store_image