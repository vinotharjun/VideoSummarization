parent_dir = "./dataset"
video_directory="./dataset/videos"
label_directory = parent_dir+"/"+"keyframes"
allframe_directory = parent_dir+"/"+"all frames"
dataset_file = "data.csv"
maxlen = 83
import os 
import pandas as pd
if os.path.exists(parent_dir+"/"+dataset_file):
    maxlen= max(pd.read_csv(parent_dir+"/"+dataset_file)["frame count"])
if __name__ == "__main__":
    if not os.path.exists("results"):
        os.mkdir("./results")
    if not os.path.exists("saved model"):
        os.mkdir("./saved model")
    


# from PIL import Image
# import numpy
# import matplotlib.pyplot as plt
# img = Image.open("./results/movie.gif").convert('RGB')
# img_arr = numpy.asarray(img.getdata(), dtype=numpy.uint8)
# img_arr = img_arr.reshape(img.size[0], img.size[1], 3) #Note the number 3
# plt.imshow(img_arr)
# plt.show()
