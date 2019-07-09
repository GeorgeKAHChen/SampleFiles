############################################################
#
#		Some useful function
#		Copyright(c) KazukiAmakawa, all right reserved.
#		Init.py
#
############################################################
"""
		FUNCTION INSTRUCTION
		
LogWrite(LogStr, kind)
	This function will write the infomation into the log file.
	
	LogStr = "Infomation You want to add"
	kind = "0" #The program worked right
	kind = "else" #ERROR else

	return None

BuildFile(FileName)
	This function will build a new file with FileName

	FileName = "The name of the file you want to build"

	return None

BuildFolder(FolderName)
	This function will build a new folder with FileName

	FileName = "The name of the folder you want to build"

	return None

MoveFile(FileLocation, NewLocation, NewName)
	This function will copy files.

	FileLocation = The location of the file (with file name)
	NewLocation = The location where you want save this file
	NewName = The FileName you want to change.
	
	return None

	#Pay attention if the location is abs path or relative path
	#This function also can be used as rename, as the usage of "mv" in bash.

StaClear()
	This function will clear the terminal (For Linux, MacOS) or command line (For Windows)
	
	return None

IntInput(Str, Min, Max, Method)
	This function will judge the input string.

	Str = "The infomation which will print"
	Min = the min of input (int / float / inf)
	Max = the max of input (int / float / inf)
	Method = "The kind of input data you need" (int / float) 
	
	return InputNumber

GetTime()
	This function will return the time as a int

	return Time

ArrOutput(Arr):
	This function will save the array as a table.

	Arr = The array you want to save

	return None

GetNextDay(Time, TimeAdd)
	This function will calculated the next day by the calendar

	Time = 19961221 (The beginning time)
	TimeAdd = 3 (The time you want to add)

	return Time+TimeAdd


SystemJudge()
	This function will return the system infomation

	return 0 means this system is not windows system
		   1 means this system is windows system


FigureInput()
	This function will get all images in the folder "Saving"

	return [Figure, Name]
		Figure is the abstract location for all images
		Name is the name for every image

GetSufixFile(dir, sufixSet)
	This function will get all file with determined sufix in the folder

	dir = the folder you want to get files
	sufixSet = [".xxx1", ".xxx2", ...] the sufix files you need

	return Files location you need 

PackageDetection(PackList)
	This function will print the package which not install

	PackList = ["package_name_1", "package_name_2", ...]

	return True means some packages not installed
		   False means all packages are installed
"""


def LogWrite(LogStr, kind):
	import os
	import time 
	FileName = "info.log"
		
	File = open(FileName, "a")
	Ima = time.ctime()
	WriteStr = '[' + Ima + ']'
	if kind == '0':
		WriteStr = WriteStr + '  Info   '
	else:
		WriteStr = WriteStr + '  Error  '
	WriteStr = WriteStr + LogStr + '\n'
	File.write(WriteStr)
	File.close()
	return 0


def IntInput(Str, Min, Max, Method):
	Int = 0
	NoMin = False
	NoMax = False
	try:
		Min = int(Min)
	except:
		NoMin = True

	try:
		Max = int(Max)
	except:
		NoMax = True
	
	while 1:
		InpStr = input(Str)
		try:
			if Method == "int":
				Int = int(InpStr)
			elif Method == "float":
				Int = float(InpStr)
		except:
			print("Input Error")
			continue
		else:
			if NoMin == True and NoMax == True:
				break
			
			elif NoMin == True and NoMax == False:
				if Int > Max:
					print("Input Error")
					continue
				else:
					break
		
			elif NoMin == False and NoMax == True:
				if Int < Min:
					print("Input Error")
					continue
				else:
					break
			else:
				if Int < Min or Int > Max:
					print("Input Error")
					continue
				else:
					break
	return Int



def GetTime():
	import time
	TimeStr = time.ctime()
	TimeStr += ' '
	Space = -1
	Jikan = ['', '', '', '']
	RemStr = ''
	for i in range (0, len(TimeStr)):
		if TimeStr[i] == ' ':
			if RemStr == '':
				continue
			else:
				if not Space == -1:
					Jikan[Space] += RemStr
				RemStr = ''
				Space += 1	
		else:
			RemStr += TimeStr[i]

	ReturnTime = 0
	try:
		ReturnTime = int(Jikan[3])
	except ValueError:
		LogWrite('Get time error', '121')
		return -1
	ReturnTime *= 100

	if Jikan[0] == "Jan":
		ReturnTime += 1
	if Jikan[0] == "Feb":
		ReturnTime += 2
	if Jikan[0] == "Mar":
		ReturnTime += 3
	if Jikan[0] == "Apr":
		ReturnTime += 4	
	if Jikan[0] == "May":
		ReturnTime += 5
	if Jikan[0] == "Jun":
		ReturnTime += 6
	if Jikan[0] == "Jul":
		ReturnTime += 7
	if Jikan[0] == "Aug":
		ReturnTime += 8	
	if Jikan[0] == "Sep":
		ReturnTime += 9
	if Jikan[0] == "Oct":
		ReturnTime += 10
	if Jikan[0] == "Nov":
		ReturnTime += 11
	if Jikan[0] == "Dec":
		ReturnTime += 12

	ReturnTime *= 100

	try:
		ReturnTime += int(Jikan[1])
	except ValueError:
		LogWrite('Get time error', '122')
		return -1

	ReturnTime *= 1000000
	DokiStr = ''
	Kanryou = 0
	Jikan[2] += ":"
	for i in range (0, len(Jikan[2])):
		if Jikan[2][i] == ':':
			Kanryou += 1
			if Kanryou == 1 or Kanryou == 2:
				continue
			else:
				try:
					ReturnTime += int(DokiStr)
				except ValueError:
					LogWrite('Get time error', '123')
					return -1
				break
			
		else:
			DokiStr += Jikan[2][i]

	return ReturnTime


def ArrOutput(Arr, Mode = 0):
	FileName = "SaveArr" + str(GetTime())
	BuildFile(FileName)
	File = open(FileName, "a")
	Str = ""
	if Mode == 1:
		Str += "[["
	for i in range(0, len(Arr)):
		for j in range(0, len(Arr[i])):
			Str += str(Arr[i][j])
			if Mode == 0:
				Str += "\t"
			elif Mode == 1 and j != len(Arr[i]) - 1:
				Str += ", "
		if Mode == 0:
			Str += "\n"
		elif Mode == 1:
			if i != len(Arr) - 1:
				Str += "], ["
			else:
				Str += "]]"
	File.write(Str)
	File.close()


def GetNextDay(Time, TimeAdd):
	Day = Time % 100
	Mouth = ((Time - Day)/100) % 100
	Year = int(Time / 10000)
	Day += TimeAdd
	
	if Mouth == 2:
		if Year % 400 == 0 or (Year % 100 != 0 and Year % 4 == 0):
			if Day > 29:
				Day -= 29
				Mouth += 1
		else:
			if Day > 28:
				Day -= 28
				Mouth += 1

	if Mouth == 1 or Mouth == 3 or Mouth == 5 or Mouth == 7 or Mouth == 8 or Mouth == 10:
		if Day > 31:
			Day -= 31
			Mouth += 1
	
	if Mouth == 4 or Mouth == 6 or Mouth == 9 or Mouth == 11:
		if Day > 30:
			Day -= 30
			Mouth += 1
	
	if Mouth == 12:
		if Day > 31:
			Day -= 31
			Mouth = (Mouth + 1) % 12
			Year += 1

	return (Year * 10000 + Mouth * 100 + Day)


def SystemJudge():
	import platform  
	Str = platform.system() 
	if Str[0] == "w" or Str[0] == "W":
		return "Dos"
	elif Str == "Darwin": 
		return "Darwin"
	else:
		return "Linux"


def GetSufixFile(dir_name, sufixSet):
	import os
	im_paths = []
	im_name = []
	for parent, dirs, files in os.walk(dir_name):
		for file in files:
			name,sufix = file.split('.')
			im_path = ""
			if sufix in sufixSet:
				im_path = os.path.join(parent,file)
			if os.path.exists(im_path):
				im_paths.append(im_path)
				im_name.append(name)

	return im_paths, im_name


def RGBList2Table(InputImage):
	import numpy as np
	Size = np.shape(InputImage)
	if len(Size) != 3:
		print("InputError: RGBList2Table function need input image with [[[R,G,B] * width] * height] parameter. Your input may RGB tabled image or grey image")
		return [[[-1]], [[]], [[]]]
	if Size[2] != 3 and Size[0] == 3:
		return InputImage

	RTable = []
	GTable = []
	BTable = []
	for i in range(0, len(InputImage)):
		RLine = []
		GLine = []
		BLine = []
		for j in range(0, len(InputImage[i])):
			RLine.append(InputImage[i][j][0])
			GLine.append(InputImage[i][j][1])
			BLine.append(InputImage[i][j][2])
		RTable.append(RLine)
		GTable.append(GLine)
		BTable.append(BLine)
	return np.array([RTable, GTable, BTable])



def ImageIO(file_dir = "", img = [], io = "i", mode = "rgb", backend = ""):
	"""
	This is a image io and print function to combined several backend
	"""
	import numpy as np

	opencv_mark	    = False
	PIL_mark        = False
	matplotlib_mark = False
	imageio_mark    = False


	if len(backend) == 0:	
		try:
			import cv2
			opencv_mark = True
		except:
			try:
				from PIL import Image
				PIL_mark = True
			except:
				try:
					import matplotlib
					matplotlib_mark = True
				except:
					try:
						import imageio
						imageio_mark = True
					except:
						ModuleNotFoundError("None image processing model has been found, you may need to install opencv, PIL, matplotlib or imageio")
	

	elif backend == "opencv":
		import cv2
		opencv_mark = True
	elif backend == "Pillow":
		from PIL import Image
		PIL_mark = True
	elif backend == "matplotlib":
		import matplotlib
		matplotlib_mark = True
	elif backend == "imageio":
		import imageio
		imageio_mark = True
	else:
		ModuleNotFoundError("Import package not be support, you may need to use opencv, PIL, matplotlib or imageio")







	if opencv_mark == True:
		print("Using opencv backend")
		import cv2



		if io == "i":
			if mode == "rgb":
				img = cv2.imread(file_dir)
			elif mode == "grey":
				img = cv2.imread(file_dir, cv2.IMREAD_GRAYSCALE)
			else:
				ValueError("mode error, the image mode must be confirmed as 'grey' for mono or 'rgp' for rgb image")
			return img



		elif io == "p":
			img = np.array(img)
			img_size = len(np.shape(img))
			if len(file_dir) == 0 and img_size != 2 and img_size != 3:
				ValueError("It is necessary to confirmed the location of image or img array if you want to print image")
			
			if len(file_dir) != 0:
				img = cv2.imread(file_dir)
			
			if mode == "rgb":
				cv2.imshow("image", img)
				cv2.waitKey(1)
			elif mode == "grey":
				img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
				cv2.imshow("image". img)
				cv2.waitKey(1)
			else:
				ValueError("mode error, the image mode must be confirmed as 'grey' for mono or 'rgp' for rgb image")
			return True



		elif io == "o":
			if len(file_dir) == 0:
				ValueError("file_dir not be confirmed")

			if mode == "rgb":
				cv2.imwrite(file_dir, img)
			elif mode == "grey":
				img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
				cv2.imwrite(file_dir, img)
			else:
				ValueError("mode error, the image mode must be confirmed as 'grey' for mono or 'rgp' for rgb image")
			return True

		else:
			ValueError("io error, the io must be confirmed as 'i' for input, 'p' for presentation or 'o' for output")







	elif PIL_mark == True:
		print("Using Pillow backend")
		from PIL import Image


		if io == "i":
			if mode == "rgb":
				img = np.array(Image.open(file_dir))
			elif mode == "grey":
				img = np.array(Image.open(file_dir).convert("L"))
			else:
				ValueError("mode error, the image mode must be confirmed as 'grey' for mono or 'rgp' for rgb image")
			return img



		elif io == "p":
			img = np.array(img)
			img_size = len(np.shape(img))
			if len(file_dir) == 0 and img_size != 2 and img_size != 3:
				ValueError("It is necessary to confirmed the location of image or img array if you want to print image")
			
			if len(file_dir) != 0:
				img = Image.open(file_dir)
			else:
				img = Image.fromarray(img.astype('uint8'), 'RGB')
			
			if mode == "rgb":
				img.show()
			elif mode == "grey":
				img = img.convert("L")
				img.show()
			else:
				ValueError("mode error, the image mode must be confirmed as 'grey' for mono or 'rgp' for rgb image")
			return True



		elif io == "o":
			if len(file_dir) == 0:
				ValueError("file_dir not be confirmed")

			img = Image.fromarray(img.astype('uint8'), 'RGB')
			if mode == "rgb":
				img.save(file_dir)
			elif mode == "grey":
				img = img.convert("L")
				img.save(file_dir)
			else:
				ValueError("mode error, the image mode must be confirmed as 'grey' for mono or 'rgp' for rgb image")
			return True

		else:
			ValueError("io error, the io must be confirmed as 'i' for input, 'p' for presentation or 'o' for output")






	elif matplotlib_mark == True:
		print("Using matplotlib backend")
		import matplotlib


		if io == "i":
			if mode == "rgb":
				img = np.array(matplotlib.pyplot.imread(file_dir))
			elif mode == "grey":
				img = np.array(matplotlib.pyplot.imread(file_dir))
				img = np.dot(img[...,:3], [0.299, 0.587, 0.144])
			else:
				ValueError("mode error, the image mode must be confirmed as 'grey' for mono or 'rgp' for rgb image")
			return img



		elif io == "p":
			img = np.array(img)
			img_size = len(np.shape(img))
			if len(file_dir) == 0 and img_size != 2 and img_size != 3:
				ValueError("It is necessary to confirmed the location of image or img array if you want to print image")
			
			if len(file_dir) != 0:
				img = np.array(matplotlib.pyplot.imread(file_dir))
			
			if mode == "rgb":
				matplotlib.pyplot.imshow(img)
			elif mode == "grey":
				img = np.dot(img[...,:3], [0.299, 0.587, 0.144])
				matplotlib.pyplot.imshow(img)
			else:
				ValueError("mode error, the image mode must be confirmed as 'grey' for mono or 'rgp' for rgb image")
			return True



		elif io == "o":
			if len(file_dir) == 0:
				ValueError("file_dir not be confirmed")

			img = Image.fromarray(img.astype('uint8'), 'RGB')
			if mode == "rgb":
				matplotlib.pyplot.savefig(img)
			elif mode == "grey":
				img = np.dot(img[...,:3], [0.299, 0.587, 0.144])
				matplotlib.pyplot.savefig(img)
			else:
				ValueError("mode error, the image mode must be confirmed as 'grey' for mono or 'rgp' for rgb image")
			return True

		else:
			ValueError("io error, the io must be confirmed as 'i' for input, 'p' for presentation or 'o' for output")











	elif imageio_mark == True:
		print("Using imageio backend")
		import imageio
		if io == "i":
			if mode == "rgb":
				img = np.array(imageio.imread(file_dir))
			elif mode == "grey":
				img = np.array(imageio.imread(file_dir))
				img = np.dot(img[...,:3], [0.299, 0.587, 0.144])
			else:
				ValueError("mode error, the image mode must be confirmed as 'grey' for mono or 'rgp' for rgb image")
			return img



		elif io == "p":
			ValueError("mode error, imageio don't have image presentation system")
			return True



		elif io == "o":
			if len(file_dir) == 0:
				ValueError("file_dir not be confirmed")

			if mode == "rgb":
				imageio.imwrite(file_dir, img)
			elif mode == "grey":
				img = np.dot(img[...,:3], [0.299, 0.587, 0.144])
				imageio.imwrite(file_dir, img)
			else:
				ValueError("mode error, the image mode must be confirmed as 'grey' for mono or 'rgp' for rgb image")
			return True

		else:
			ValueError("io error, the io must be confirmed as 'i' for input, 'p' for presentation or 'o' for output")

	else:
		ModuleNotFoundError("None image processing model has been found, you may need to install opencv, PIL, matplotlib or imageio")






