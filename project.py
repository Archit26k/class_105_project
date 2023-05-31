# importing ......
import os
import cv2

# Declaring path and lists .......
path   = "Images"
images = []

# Using For in Loop to get the name of image files ........
for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name = path+'/'+file
        print(file_name)
        images.append(file_name)

# To display video ........
count = len(images)
frame= cv2.imread(images[0])
height,width,channels = frame.shape

size = (width,height)
print(size)

output2 = cv2.VideoWriter("friends.mp4" ,cv2.VideoWriter_fourcc(*'DIVX'),0.8 , size )

for i in range(count-1,0,-1):
    cv2.waitKey(1)
    frame = cv2.imread(images[i])
    output2.write(frame)


output2.release() 


