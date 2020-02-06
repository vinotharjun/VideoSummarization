import cv2
import os
import glob
import re
from env_variable import parent_dir,video_directory
def extract_frames(video_file_path):
    print(video_file_path)
    if not os.path.exists:
        print(video_file_path,"is not exists")
        return
    vidcap = cv2.VideoCapture(video_file_path)
    success,image = vidcap.read()
    count = 1
    success = True
    frame_list = []
    all_frames_path = os.path.join(parent_dir,"all frames") 
    if not os.path.exists(all_frames_path):
        os.mkdir(all_frames_path)
    video_id = re.findall(r'\d+',video_file_path )[0]
    video_id_path = os.path.join(all_frames_path,video_id)
    if not os.path.exists(video_id_path):
        os.mkdir(video_id_path)
 
    while success:
        cv2.imwrite(video_id_path+"/frame%d.jpg" % count, image)
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        count += 1
        print(count)    
    
def extract_all_videos(video_directory=video_directory):
   
    for video in os.listdir(video_directory):
        print(video)
        extract_frames(os.path.join(video_directory,video))
        
if __name__ =="__main__":

    extract_all_videos()






'''
def extract_images(filepath,dir=""):
    vidcap = cv2.VideoCapture(dir+"/"+filepath)
    success,image = vidcap.read()
    count = 1
    success = True
    frame_list=[]
    parent_dir = "./dataset"
    if not os.path.exists(parent_dir):
        os.mkdir(parent_dir)
    if not os.path.exists(parent_dir+"/all frames"):
        os.mkdir(parent_dir+"/all frames")
    video_id = re.findall(r'\d+',filepath )[0]
    if not os.path.exists(parent_dir+"/all frames/"+video_id):
        os.mkdir(parent_dir+"/label/"+video_id)
    
    path =os.path.join(parent_dir,video_id,"all frames")
    print(path)
    while success:
        print(path+"/frame%d.jpg" % count)
        cv2.imwrite(path+"/frame%d.jpg" % count, image)     #
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        count += 1
        print(count)
def extract_all_videos(directory):
    for single_dir in os.listdir(directory):
        extract_images(single_dir,directory)

# extract_all_videos("./dataset/videos")
'''