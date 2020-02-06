import pandas as pd
import numpy as np
from glob import glob
import os
import re
import skvideo.io  
from skimage.transform import resize
import skimage
from env_variable import parent_dir,video_directory,label_directory,allframe_directory
#specifying path
dataset_path = parent_dir
videos_path = video_directory
labels_path = label_directory
# maxlen =86
def convert_csv(dataframe, filename):
    dataframe.to_csv(filename,index=False)
def make_csv(dataset_path=dataset_path,videos_path=videos_path,labels_path=labels_path,filename="data.csv"):
    dataframe = pd.DataFrame()
    videos_path_list = [ i for i in glob(videos_path+"/*.mp4")]
    dataframe["videos"] = videos_path_list
    dataframe["frame count"] = [ len(os.listdir(i)) for i in glob(allframe_directory+"/*")]
    frame_importance=[]
    for i in  glob(labels_path+"/*"):
        list_frames=[]
        for j in os.listdir(i):
            number = re.findall(r'\d+', j)[0]
            list_frames.append(number)
        string =','.join(list_frames)
        frame_importance.append(string)
    dataframe["important frames"]= frame_importance
    convert_csv(dataframe,dataset_path+"/"+filename)

if __name__ == "__main__":
    make_csv()    
    print("dataset stored in ",parent_dir)
    