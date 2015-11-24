'''rotate.py takes in an image sequence of a sample being physically rotated through
some angle. Then, it preforms a reverse rotation, so that all the images have
the same orientation. This is useful if the experimentalist just wants to focus on 
light intensity changes as a function of rotation, and doesn't want to get
distracted.'''

import argparse
import matplotlib.pyplot as plt
import numpy as np
import math
import glob
from scipy.ndimage.interpolation import rotate
import os 
#Take FileName of image

#Create Folder to store rotated images
if not os.path.exists("./rotatedImages"):
    os.makedirs("./rotatedImages")

names = glob.glob('./*.tif')
frames =[plt.imread(name) for name in names]
#Now, we need to extract the rotation information from the filename.
f, (ax1,ax2) = plt.subplots(ncols=2, nrows=1, figsize=(18,9))
ax1.imshow(frames[0],cmap='gray')
#plt.show()
angle = []
for name,frame in zip(names,frames):
    print "Image "+name.strip("./")
    theta = input( "What is the angle of the rotation stage for this image?")
    angle = np.append(angle,float(theta))
    rotated = rotate(frame,float(theta),reshape=True)
    plt.imsave("./rotatedImages/rotated-"+name.strip("./"),rotated, vmin=None,cmap='gray')

