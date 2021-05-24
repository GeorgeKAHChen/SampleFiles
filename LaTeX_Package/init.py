#latex auto compile
#By Kazuki Amakawa
#Initial
def main():
    import os
    os.system("clear")
    os.system("clear")
    para1 = ""
    while 1:
        para1 = input("Language choice: \nzh: Chinese, \njp: Japanese,\nen: English\n")
        if para1 == "zh" or para1 == "jp" or para1 == "en":
            break
        else:
            print("Input Error!")

    para2 =  ""
    while 1:
        para2 = input("normal(n)/presentation(p):\t\t\t")
        if para2 == "n" or para2 == "p":
            break
        else:
            print("Input Error!")

    files = ["Chinese.tex", "English.tex", "Japanese.tex", "Presentation.tex"]
    if para1 == "zh" and para2 == "n":
        files[0] = ""
        filename = "Chinese"
    if para1 == "en" and para2 == "n":
        files[1] = ""
        filename = "English"
    if para1 == "jp" and para2 == "n":
        files[2] = ""
        filename = "Japanese"
    if para1 == "zh" and para2 == "p":
        files[3] = ""
        filename = "Presentation"
    if para1 == "en" and para2 == "p":
        files[3] = ""
        filename = "Presentation"
    if para1 == "jp" and para2 == "p":
        files[3] = ""
        filename = "Presentation"

    for i in range(0, len(files)):
        cmd = "rm -rf " + files[i]
        os.system(cmd)
    os.system("rm -rf makefile")

    string = ""
    string += "#Auto Latex Compile\n"
    string += "#Copyright by Kazuki Amakawa\n"
    string += "\n"
    string += "filename=" + filename + "\n"
    string += "main:\n"
    if para1 == "zh" or para1 == "jp":
        string += "\txelatex ${filename}.tex\n"
        string += "\txelatex ${filename}.tex\n"
        string += "\txelatex ${filename}.tex\n"
        string += "\trm -rf ${filename}.{ps,log,aux,out,dvi,bbl,blg,thm,toc,nav,snm}\n"
        string += "\topen ${filename}.pdf\n"
    elif para1 == "en":
        string += "\tlatex ${filename}.tex\n"
        string += "\tlatex ${filename}.tex\n"
        string += "\tlatex ${filename}.tex\n"
        string += "\trm -rf ${filename}.{ps,log,aux,out,dvi,bbl,blg,thm,toc,nav,snm}\n"
        string += "\topen ${filename}.pdf\n"
    string += "\n"
    string += "ref:\n"
    if para1 == "zh" or para1 == "jp":
        string += "\txelatex ${filename}.tex\n"
        string += "\tbibtex ${filename}.aux\n"
        string += "\txelatex ${filename}.tex\n"
        string += "\txelatex ${filename}.tex\n"
        string += "\trm -rf ${filename}.{ps,log,aux,out,dvi,bbl,blg,thm,toc,nav,snm}\n"
        string += "\topen ${filename}.pdf\n"
    elif para1 == "en":
        string += "\tlatex ${filename}.tex\n"
        string += "\tbibtex ${filename}.aux\n"
        string += "\tlatex ${filename}.tex\n"
        string += "\tlatex ${filename}.tex\n"
        string += "\trm -rf ${filename}.{ps,log,aux,out,dvi,bbl,blg,thm,toc,nav,snm}\n"
        string += "\topen ${filename}.pdf\n"
    string += "\n"
    string += "e:\n"
    if para1 == "zh" or para1 == "jp":
        string += "\txelatex ${filename}.tex\n"
        string += "\trm -rf ${filename}.{ps,log,aux,out,dvi,bbl,blg,thm,toc,nav,snm}\n"
        string += "\topen ${filename}.pdf\n"
    elif para1 == "en":
        string += "\tlatex ${filename}.tex\n"
        string += "\trm -rf ${filename}.{ps,log,aux,out,dvi,bbl,blg,thm,toc,nav,snm}\n"
        string += "\topen ${filename}.pdf\n"
    string += "\n"

    string += "clear:\n"
    string += "\trm -rf ${filename}.pdf\n"

    FileName = "makefile"
    File = open(FileName, "w")
    File.write(string)
    File.close()
    os.system("clear")
    os.system("rm -rf init.py")
    print("Latex initial finished")
        

if __name__ == '__main__':
    main()

