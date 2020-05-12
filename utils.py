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
from keras.models import Model, Input
from keras.applications.vgg16 import preprocess_input,VGG16
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import LSTM,Dense,TimeDistributed,Bidirectional,Input,Conv3D,AveragePooling3D,GlobalAveragePooling2D,Flatten,GlobalAvgPool3D,GlobalAveragePooling2D,GlobalAveragePooling3D
from env_variable import *
def read_single_video(video_path):
    videodata = skvideo.io.vread(video_path)
    return videodata
  
def resize_image(data,size=224):
  X_data_resized = [ cv2.resize(image, (size,size)) for image in data]
  x = np.asarray(X_data_resized)
  return x

def extract_feature(data,feat_extractor):
    # print(data.shape)
    x = preprocess_input(data)
    features = feat_extractor.predict(x)
    print(features.shape)
    return features

def pad_data(data):
  data = np.expand_dims(data, axis=0)
  padded_data = pad_sequences(data,maxlen=maxlen,padding = 'post')
  return padded_data

def read_all_videos(dataset,feat_extractor):
  video_array =[]
  for i in dataset.iterrows():
    video_path = dataset.iloc[i[0]]["videos"]
    videodata = read_single_video(video_path)
    videodata = resize_image(videodata).astype(np.float64)
    feature    = extract_feature(videodata,feat_extractor)
    print(feature)
    del videodata
    feature = pad_data(feature)
    video_array.append(feature)
    print(i[0])    
  features = np.vstack(video_array) 
  del video_array
  return features

def one_hot_encoding(total_frames,key_frames):
  one_hot_vector = np.zeros(maxlen)
  one_hot_vector[key_frames]=1
  return one_hot_vector


def get_labels(dataset):
  labels =[]
  for i in dataset.iterrows():
    total_frames = dataset.iloc[i[0]]["frame count"]
    key_frames =dataset.iloc[i[0]]["important frames"]
    key_frames = [int(e) if e.isdigit() else e for e in key_frames.split(',')]
    key_frames.sort()
    key_frames= np.array(key_frames)
    key_frames = key_frames-1
    labels.append(one_hot_encoding(total_frames,key_frames))
  labels= np.array(labels)
  labels = np.expand_dims(labels,axis=2)
  return labels

