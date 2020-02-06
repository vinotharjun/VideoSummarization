import imageio
from utils import *
from model import get_model,get_vgg_model
import re
import numpy as np
from env_variable import *

def extract_feature_single(video_path):

  model = get_model(mode="test")
  feature_extractor = get_vgg_model()
  videodata = read_single_video(video_path)
  videodata = resize_image(videodata)
  videodata = pad_data(videodata).squeeze()
  feature    = extract_feature(videodata,feature_extractor)
  output= model.predict(np.expand_dims(feature,0)).squeeze()
  print(output)
  return np.nonzero(output>=0.5)[0]


def get_summarized_video(video_path,jupyter=None):
  video_id =  re.findall(r'\d+', video_path)[0]
  key_frame = extract_feature_single(video_path)
  key_frame = key_frame + 1
  print("important frames",key_frame)
  gifs =[]
  for i in os.listdir(allframe_directory+"/"+video_id):
    frame_id =  int(re.findall(r'\d+', i)[0])
    if frame_id in key_frame:
    
      filename = allframe_directory+"/"+video_id+"/"+i
      print(filename)
      gifs.append( imageio.imread(filename))
  imageio.mimsave('./results/result video.gif', gifs)
if __name__=="__main__":
    print("prediction started")
    path= "/media/vinodarjun/Storage/deeplearning Projects/computer vision/summary/dataset/videos/1.mp4"
    get_summarized_video(path)
    print("summary video saved in results folder")