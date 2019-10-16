import cv2
import numpy as np
import os
from os.path import isfile, join
import natsort
fil=[]
pathIn = 'C:/Users/jithu/PycharmProjects/j/im/'
pathOut = 'abit.mp4'
fps = 25
frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
# for sorting the file names properly
#files.sort(key=lambda x: x[5:-4])
fil=natsort.natsorted(files, reverse=False)
print(fil)
#files.sort()
frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
# for sorting the file names properly
files.sort(key=lambda x: x[5:-4])
for i in range(len(files)):
    filename = pathIn + fil[i]
    # reading each files
    #print(filename)
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)

    # inserting the frames into an image array
    frame_array.append(img)
out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()