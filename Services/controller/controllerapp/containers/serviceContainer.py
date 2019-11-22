# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 21:33:51 2019

@author: louie.bafford
"""

class Container():
    def __init__(self):
        #Literals
        self.image_bucket = 'cnn-images'
        self.cnn_host = 'CNNSVC_SERVICE_HOST'
        self.cnn_port = 'CNNSVC_SERVICE_PORT'
        self.cnn_url = 'prediction'