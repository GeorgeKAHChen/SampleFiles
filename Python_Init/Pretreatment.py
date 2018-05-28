############################################################
#
#		Image Processing - Algorithms
#		Copyright(c) KazukiAmakawa, all right reserved.
#
############################################################
"""
		FUNCTION INSTRUCTION
		
This file will include some common image processing pretreatment and
after treatment
FileImport(FileLocation)
	This function will import a image file and determine the location of file

	FileLocation = "The location of file you want to import"

	return image array

"""
def FileImport(FileLocation):
	from PIL import Image
	import numpy as np
	import os 

	if not os.path.exists(FileLocation):
		print("File not exist")
		return np.array([-1])
	else:
		return np.array(Image.open(FileLocation).convert("L"))





def Histogram(img):
	Statistic = [0 for n in range(258)]
	Probability = [0.00 for n in range(258)]
	TTL = 0

	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			Statistic[img[i][j]] += 1
			TTL += 1

	for i in range(0, len(Statistic)):
		Probability[i] = Statistic[i] / TTL

	return Probability





def Thresholding(img, TSH, TSH2):
	import cv2
	TemImg = [[0.00 for n in range(len(img[0]))] for n in range(len(img))]
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			if img[i][j] < TSH or img[i][j] > TSH2:
				TemImg[i][j] = 0
			else:
				TemImg[i][j] = 255

	return cv2.Canny(np.uint8(TemImg), 85, 170)



