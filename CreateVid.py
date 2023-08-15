import os
import cv2


path = "C:/Users/IPSHITA/Desktop/Whjr/p105/Images"

Images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print("FILE NAME : " , file_name)
               
        Images.append(file_name)
        
print("LENGTH OF THE LIST OF IMAGES : ",len(Images))

count = len(Images)

frame = cv2.imread(Images[0])

height, width, channels = frame.shape 
size = (width,height) 
print("SIZE OF THE FRAME : ", size) 

out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size) 

for i in range(0,count-1):
     frame = cv2.imread(Images[i]) 
     out.write(frame) 

out.release()