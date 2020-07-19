import cv2
from env_variable import maxlen
import pandas as pd
import numpy as np
from glob import glob
import os
import re
# !pip install scikit-video
# !apt-get install --no-install-recommends ffmpeg
import skvideo.io  
from skimage.transform import resize
import skimage
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
import keras
from PIL import Image
from model import get_vgg_model
from keras.models import Model, Input
from keras.applications.vgg16 import preprocess_input,VGG16
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import LSTM,Dense,TimeDistributed,Bidirectional,Input,Conv3D,AveragePooling3D,GlobalAveragePooling2D,Flatten,GlobalAvgPool3D,GlobalAveragePooling2D,GlobalAveragePooling3D
from env_variable import *



def extract_feature(data,feat_extractor):
    # print(data.shape)
    x = preprocess_input(data)
    features = feat_extractor.predict(x)
    print(features.shape)
    return features
    
def resize_image(data,size=224):
    X_data_resized = [ cv2.resize(image, (size,size)) for image in data]
    x = np.asarray(X_data_resized)
    return x

def read_image(path1,path2):
``  x1 = cv2.resize(np.array(Image.open(path1).convert("RGB")),(224,224))
    x2 = cv2.resize(np.array(Image.open(path2).convert("RGB")),(224,224))
    return x1,x2
  
  
if __name__ == '__main__':
    path1 = "./dataset/all frames/1/frame1.jpg"
    path2 = "./dataset/all frames/1/frame2.jpg"
    for path2 in os.listdir("./dataset/all frames/1/"):
        path2 = "./dataset/all frames/1/"+path2
        x1,x2 = read_image(path1,path2)
        model = get_vgg_model()
        x1 = extract_feature(x1,model)
        x2 = extract_feature(x2,model)
        print("distance between path1 and path2 ====> ",np.linalg.norm(x1-x2))
 
        
