#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import cv2
from os import listdir
from os. path import isfile, join


# In[2]:


docpath = r'your_windows_path' #change path  your_windows_path 

docfiles = [f.upper() for f in listdir(docpath) if isfile(join(docpath, f))]
#docfiles = [f.upper() for f in docfiles]
doc = [f for f in docfiles if '.JPG' in f[-4:]]

path = []
file = []
result_pic = []


# In[3]:


for i in doc:
    
    image = cv2.imread(rf'{docpath}\{i}')
    
    r = 1200.0 / image. shape[1]
    dim = (1200, int(image. shape[0] + r))
    
    image_resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    
    # of the image
    (h, w) = image_resized. shape[:2]
    center = (w / 2, h / 2)
    scale = 0.6
    
    # rotate the image by 360 degrees
    M_1 = cv2.getRotationMatrix2D(center, 360, scale)
    img_1 = cv2.warpAffine(image_resized, M_1, (w, h))
    #rotate the image by 90 degrees
    M_2 = cv2.getRotationMatrix2D(center, 90, scale)
    img_2 = cv2.warpAffine(image_resized, M_2, (w, h))
    # rotate the image by 180 degrees
    M_3 = cv2.getRotationMatrix2D(center, 180, scale)
    img_3 = cv2.warpAffine(image_resized, M_3, (w, h))
    # rotate the image by 270 degrees
    M_4 = cv2.getRotationMatrix2D(center, 270, scale)
    img_4 = cv2.warpAffine(image_resized, M_4, (w, h))
    
    tolerance = 0
    
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    def rotation_img(img):
        
    # Read the image
        image = img
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        
        )
            
            
        l_id = len(faces)
        return l_id
    
    
    check_0 = int(rotation_img(img_1)) + int(rotation_img(img_2)) + int(rotation_img(img_3)) + int(rotation_img(img_4))
    
    if check_0 > 0:
        check = 1
    else:
        check = 0
        
    #print(check)
    
    path.append((rf'{docpath}\{i}'))
    file.append(i)
    result_pic.append(check)


# In[4]:


summary_list = list(zip(path, file, result_pic))


# In[6]:


summary_df = pd. DataFrame (summary_list, columns = ('sciezka', 'plik', 'wynik'))
summary_df.to_excel("ID_check.xlsx",
sheet_name='ID_check_')

