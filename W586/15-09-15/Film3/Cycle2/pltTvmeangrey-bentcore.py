#Program: Plotting mean-grey value of images from imagej vs Temperature

'''Takes two data files, and plots the relevant mean-grey v Temp'''

import sys
import os
import numpy as np
import math
import matplotlib.pyplot as plt
import argparse
from scipy import interpolate

parser = argparse.ArgumentParser(description='Plotting meangrey v Temp')

parser.add_argument('filemean',help="Input file name of meangrey (xy)")
parser.add_argument('filetemp',help="Input file name of temp v time (xy)")
parser.add_argument('fps',help="frames per second")
args = parser.parse_args()


meangrey = np.loadtxt(args.filemean,unpack=True )
temp = np.loadtxt(args.filetemp,unpack=True, skiprows =4)

normalized_temp = temp[0]-np.min(temp[0])


#Create Interpolating Function for Temperature(time)

f = interpolate.interp1d(normalized_temp,temp[1])

grey = meangrey[1]
print args.fps
grey_Time = meangrey[0]*1./float(args.fps)
grey_Temp = f(meangrey[0]/float(args.fps))
plt.plot(grey_Temp, grey)
plt.show()
