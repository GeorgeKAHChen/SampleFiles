############################################################
#
#		Image Processing - Algorithms
#		Copyright(c) KazukiAmakawa, all right reserved.
#
############################################################
#import head
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import os.path
import math
import matplotlib.patches as patches
from scipy import misc
from collections import deque
from PIL import ImageFilter
import cv2
from copy import deepcopy


def Algorithm(location, filename = "./Output/SampleOutput.png"):
	img = np.array(Image.open(location))
	"""
	Main Algorithm
	"""
	misc.imsave(filename, img)


if __name__ == '__main__':
	import sys
	import os
	if len(sys.argv) == 1:
			print("Parameter input error, input `python3 ImageIO.py help` to get help list")
			os._exit(0)
	if not os.path.exists("./Output"):
		os.system("mkdir ./Output")

	if sys.argv[1] == "help":
		if not os.path.exists("help.sh"):
			print("\nUsage\n==============================\n\npython3 ImageIO.py  <InputFileLocation>  (OutputFileLocation)\n\n==============================\nIf you do not input the OutputFileLocation, the file will be saved in `./Output/SampleOutput`\n")
		else:
			os.sysystem("sh help.sh")
		os._exit(0)
	else:
		location = sys.argv[1]
		if len(sys.argv) == 3:
			filename = sys.argv[2]
	
	if len(sys.argv) == 2:
		Algorithm(location)
	else:
		Algorithm(location, filename)