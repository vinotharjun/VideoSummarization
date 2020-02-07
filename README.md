# VideoSummarization
An spatiotemproal modeling for video summarization by key frames extraction 

## Overview
In hospitals, medical videos are recorded which are huge and consume
lot of space. These videos are generally stored for diagnosis, treatment or
research purposes. But due to increasing number of videos it becomes difficult to
manage them. A video contains only a few frames which actually contains valid
and useful information. Hence in order to reduce the redundant frames, Video
Summarization is needed. Video summarization can be done by extracting key
frames or by shot segmentation. Summarization of these medical videos helps to
save space and time. In this  work, deep learning neural networks such as
Convolutional Neural network (CNN) and Recurrent Neural network (RNN) are
used to extract the spatiotemporal features of the videos. CNNs take the video
frames as input and the features of video are generated as output. Bidirectional
long short term memory (LSTM), a special type of RNN, is used to process the
sequential structure of video. Multilayer Perceptron is used to generate
importance scores or frame scores ranging from 0 to 1 based on which key
frames are extracted.

## Model Architecture
![Model image](https://raw.githubusercontent.com/vinotharjun/VideoSummarization/master/images/Screenshot%20from%202020-02-06%2009-01-11.png)

## Dataset details
The dataset of the endoscopy medical videos  is hard to get , so for now we annotated the manually the existing endoscopy videos,butfor different video summarization related problem this repository will work well,

### Data samples
Here is the sample data  details
Orignal video's frames after extracting 

![](https://raw.githubusercontent.com/vinotharjun/VideoSummarization/master/images/Screenshot%20from%202020-02-07%2008-31-01.png)

original video with 70 frames after summarizing 

![watch video](https://raw.githubusercontent.com/vinotharjun/VideoSummarization/master/results/result%20video.gif)

## Installation guide
will be updated




