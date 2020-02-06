import pandas as pd
import numpy as np
from glob import glob
import os
# import re
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
from keras.models import load_model
import numpy as np
from model import get_vgg_model
from utils import *
import csv
import numpy as np
def extract_features():
    model = get_vgg_model()
    dataset = pd.read_csv("./dataset/data.csv")
    features = read_all_videos(dataset,model)
    print(features.shape)
    return features
if __name__ == '__main__':

    fil_name = './resutls/features'
    example = extract_features()
    example = example.tolist()
    with open(fil_name+'.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(example)

#to read file you saved
    with open(fil_name+'.csv', 'r') as f:
        reader = csv.reader(f)
        examples = list(reader)

    print(examples)
    nwexamples = []
    for row in examples:
        nwrow = []
        for r in row:
            nwrow.append(eval(r))
        nwexamples.append(nwrow)
    print(nwexamples)


