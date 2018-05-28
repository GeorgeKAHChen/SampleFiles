############################################################
#
#		Auto LaTeX Compile
#		Copyright(c) KazukiAmakawa, all right reserved.
#		LaTeX.sh
#
############################################################
#Just for shell bash and unix
def GetFiles():
	import os
	Name = []
	for root, dirs, files in os.walk(os.getcwd()):
		for i in range(0, len(files)):
			Hajimari = 0
			Last = ""
			First = ""
			Switch = False
			
			for j in range(len(files[i]) - 1, -1, -1):
				if files[i][j] == "." and Switch == False:
					Switch = True
					continue

				else:
					if Switch == False:
						Last = files[i][j] + Last
					else:
						First = files[i][j] + First

			if Last == "tex":
				Name.append(First)

	if len(Name) == 0:
		print("No Figure")
		return -1

	print("FileLise: ")
	for i in range(0, len(Name)):
		print(str(i+1) + "\t" + Name[i] + ".tex")

	return Name


def AutoLaTeX():
	import os
	Name = GetFiles()
	for i in range(0, len(Name)):
		try:
			os.system("xelatex " + Name[i] + ".tex")
		except:
			continue
		try:
			os.system("bibtex " + Name[i] + ".aux")
		except:
			continue
		try:
			os.system("xelatex " + Name[i] + ".tex")
		except:
			continue	
		try:	
			os.system("xelatex " + Name[i] + ".tex")
		except:
			continue		
		try:
			os.system("rm " + Name[i] + ".aux")
		except:
			pass
		try:
			os.system("rm " + Name[i] + ".bbl")
		except:
			pass
		try:
			os.system("rm " + Name[i] + ".blg")
		except:
			pass
		try:
			os.system("rm " + Name[i] + ".log")
		except:
			pass
		try:
			os.system("rm " + Name[i] + ".out")
		except:
			pass
		try:
			os.system("rm " + Name[i] + ".toc")
		except:
			pass
		try:
			os.system("rm " + Name[i] + ".toc")
		except:
			pass
		try:
			os.system("rm " + Name[i] + ".thm")
		except:
			pass
		os.system("clear")
		print("Latex File " + Name[i] + " Compile Succeed!!")


AutoLaTeX()