# GTA_2_Real
The OpenCV part of the project
## USAGE:
Typical call may look like: ```python walk_testing.py -fr 2 -dim 256 --input_directory "path/to/videos" --output_directory "path/to/save"```
## ARGUMENTS:
#### 1) frame rate (-fr) - how much frames per second of video will be extracted. Default is frame for each 2 seconds
#### 2) Input path (--input_directory) - the directory there the videos are stored. The program will crawl through this directory and all inner directories ans colect paths to videos.
#### 3) Output path (--output_directory) - the directory there the resulting frames will be stored
#### 4) Dimension (-dim) - the required dimension of the resulting frames. The frames will have the qunadratic dimension. Default value is 256
## REQUIREMENTS:
#### 1) OpenCV library

## Special acknowledgments
To Chris Fotache for his knowledge, advices and great articles. Link: https://towardsdatascience.com/object-detection-and-tracking-in-pytorch-b3cf1a696a98
To Joseph Redmon and Ali Farhadi for their great model named YOLO. Link: https://pjreddie.com/darknet/yolo/
To Alex Bewley for his part in developing the SORT algorithm and its implemantation. Link: https://github.com/abewley/sort
