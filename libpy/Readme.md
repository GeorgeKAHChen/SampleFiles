# SampleFiles/libpy/Init.oy

Here are some sample functions in python I ofter use.

### LogWrite(LogStr, kind)
* WARNING: KEEPING THIS FUNCTION BECAUSE SOME OLD CODE MAY NEED IT. DO NOT USE IT ANY MORE

### IntInput(Str, Min, Max, Method)
This function will keep the input in the confident interval.

---|---
Usage
---|---
Str              | Print string when you input the value
---|---
Min              | Minimum value of the interval (as string)
---|---
Max              | Maximum value of the interval (as string)
---|---
Method           | Setting "int" for int vals and "float" for float
---|---

### GetTime()
This function will return time as long int e.g 20180102193005

### ArrOutput(Arr, Mode = 0)
An useful tool if you want to output an 2d string.

---|---
Usage
---|---
Arr              | 2d array which will be output
---|---
Mode             | Setting 0 for output the array with tab and enter which you can copy to excel directly or setting 1 for output the string with enter directly 
---|---

### GetNextDay(Time, TimeAdd)
USELESS, JUST FOR FUN

### SystemJudge()
This function will return the current system, return "Dos" as windows or Dos, return "Darwin" a Darwin or macOS, return "Linux" as Ubuntu, Debain and other linux system

### GetSufixFile(dir_name, sufixSet)
An excellent fucntion which will confirm the files with certain sufix.

|Usage|
|---|:---|
|dir_name         | The location you want to search|
|sufixSet         | An array of sufix strings which you want to search, e.g. ["png", "jpg", "avi"]|

---|---
Return (In order)
---|---
im_paths         | The location of goal files
---|---
im_name          | The name stirng(without sufix) of files
---|---

* WARNING: THIS FUNCTION STILL HAVE A LITTLE BUT. IT IS NECESSARY TO DETERMINE THAT THE GOAL HAVE NO FILE NAMED WITH ".", E.G. IF THERE IS A HIDDEN FILE IN THE GOAL FOLDER, THE PROJECT WILL SHUT DOWN DIRECTLY

### RGBList2Table(InputImage)
A tool which can change channel last images to channel first for most deep learning network.

### ImageIO(file_dir = "", img = [], io = "i", mode = "rgb", backend = "")
STUPID PYTHON!

There are several structure for image processing, opencv, pillow and others, most of then have identity image io method and python have imageio package either. It is difficult to confirm which backend can be used in goal enviroment and how to establish image io function in goal backend. In spite of this, I wrote this function for integrate the image input, output and present methods.

---|---
Usage
---|---
file_dir         | Location of Input image or Location of Output
---|---
img              | Image array for output or print in screen
---|---
io               | Working method, "i" for input, "o" for output and "p" for present on the screen
---|---
mode             | Result of image, "rgp" for RGP(BGR in opencv) image and "grey" for grey image
---|---
Backend          | Appoint the backend, you can using "opencv", "Pillow", "matplotlib" or "imageio" directly. *
---|---

* WARNIGN: IF YOU DO NOT APPOINT THE BACKEND, THIS FUNCTION WILL USING BACKEND IN ORDER OF opencv, Pillow, matplotlib the imageio. IF YOUR SYSTEM DO NOT HAVE ANY OF THEM, THE PROGRAM WILL BE TERMINATED
---|---
