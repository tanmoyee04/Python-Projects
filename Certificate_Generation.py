# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:57:48 2020

@author: Tanmoyee
""""
from PIL import Image,ImageDraw,ImageFont
img=Image.open("./CertificateTemplate.jpg")
import mathplotlib.pyplot as plt
import numpy as np
def print_img(img):
  plt.imshow(np.array(img))
  plt.show()
import cv2
#from google.colab.patches import cv2_imshow
img=cv2.imread("./CertificateTemplate.jpg")