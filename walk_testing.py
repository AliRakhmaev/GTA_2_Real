import os
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-fr", "--frame_rate", type=int, default=2,
                help="How much frames per second to extract")
ap.add_argument("-in", "--input_directory",
                help="path to directory to expore for videos")
ap.add_argument("-out", "--output_directory",
                help="path to directory to save the frames")
ap.add_argument("-dim", "--dimension", type=int, default=256,
                help="required dimension for frames")
args = ap.parse_args()

print("Here")
# Specify the path where to locate the frames
directory = os.path.abspath(args.output_directory)
print("Here2")
total_video_files = []
# Specify the path to the directory with videos. The script will go through all the inner directories and will capture the paths to the videos.
for dirpath, dirnames, files in os.walk(os.path.abspath(args.input_directory)):
    for file in files:
        total_video_files.append(os.path.join(dirpath,file))

print(total_video_files)
print("Total videos: " + str(len(total_video_files)))

# Change the current directory
# to specified directory
os.chdir(directory)
dim = (args.dimension, args.dimension)
image_count = 0

for video_file in total_video_files:
    video_name = video_file.split('\\')[-2] +'_'+ video_file.split('\\')[-1].split('.')[0]
    print(video_name)
    vidcap = cv2.VideoCapture(os.path.abspath(video_file))
    def getFrame(sec):
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = vidcap.read()
        if hasFrames:
            # resize image
            resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
            cv2.imwrite("image"+video_name+"number"+str(count)+".jpg", resized)     # save frame as JPG file
        return hasFrames
    sec = 0
    frameRate = args.frame_rate #//it will capture image in each 2 seconds
    count=1
    success = getFrame(sec)
    image_count += 1
    print("Success: " + str(success))
    while success:
        image_count += 1
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)
    print(video_file + " finished")
print("Total number of pictures: " + str(image_count))