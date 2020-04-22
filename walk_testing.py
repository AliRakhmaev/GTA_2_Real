import os
import cv2

# Specify the path where to locate the
directory = os.path.abspath('D:\DS project\Datasets\AIR_project\dataset\gtaToReal\TestB')
total_video_files = []
# Specify the path to the directory with videos. The script will go through all the inner directories and will capture the paths to the videos.
for dirpath, dirnames, files in os.walk(os.path.abspath('D:\DS project\Datasets\Real_UCF_Dataset\Assault')):
    for file in files:
        total_video_files.append(os.path.join(dirpath,file))

print(total_video_files)
print("Total videos: " + str(len(total_video_files)))

# Change the current directory
# to specified directory
os.chdir(directory)
dim = (256, 256)
image_count = 0

for video_file in total_video_files[-2:]:
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
    frameRate = 2 #//it will capture image in each 2 seconds
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

# for dirpath, dirnames, files in os.walk(os.path.abspath('D:\DS project\Datasets\GTA_Dataset\Assault')):
#     total_video_files.extend(files)
# for dirpath, dirnames, files in os.walk(os.path.abspath('D:\DS project\Datasets\GTA_Dataset\Vandalism')):
#     total_video_files.extend(files)