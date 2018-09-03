# -*- coding: utf-8 -*-
"""
Created on Mon May 21 19:04:58 2018

@author: anjalidharmik
"""


from PIL import Image
import cv2
import pytesseract
import numpy as np
import os
from datetime import datetime


def OCR_converter(src_path,folder_name,filename):
    
    print(src_path+filename)
    img = Image.open(src_path+filename)  
    
    width, height = img.size
    im2 = img.resize((int(width*10), int(height*10)), Image.ANTIALIAS)
    img.save(src_path+filename)
    im2.save(src_path+"scalled_image.jpg", quality=95)#dpi=(300.0,300.0))#quality=95)
    print("scalling done...")
    
    img = cv2.imread(src_path+"scalled_image.jpg")
#        
    # Convert to gray
    b_w = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(src_path + "gray.jpg", img)
    print("written gray image...")
    
    ret, new_img = cv2.threshold(b_w, 128, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    cv2.imwrite(src_path+'bw_image.png', new_img)
    
    inv = 255 - ret    
    horizontal_img = new_img
    vertical_img = new_img
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (100,1))
    horizontal_img = cv2.erode(horizontal_img, kernel, iterations=2)
    horizontal_img = cv2.dilate(horizontal_img, kernel, iterations=2)
    
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,100))
    vertical_img = cv2.erode(vertical_img, kernel, iterations=3)
    vertical_img = cv2.dilate(vertical_img, kernel, iterations=3)
    
    mask_img = horizontal_img + vertical_img
    no_border = np.bitwise_or(b_w, mask_img)
    cv2.imwrite(src_path+'bw_image.png', no_border)
 
    result = pytesseract.image_to_string(no_border, lang='eng')
#    print(result)
    return result
