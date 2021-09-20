#latex auto compile
#By Kazuki Amakawa
#Initial

def SystemJudge():
    import platform  
    Str = platform.system() 
    if Str[0] == "w" or Str[0] == "W":
        return "Dos"
    elif Str == "Darwin": 
        return "Darwin"
    else:
        return "Linux"


def main():
    import os
    import time 

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
    os.system("mv *.tex main.tex")

    curr_sys = SystemJudge()
    String = ""
    
    FileName = "makefile_pre"
    File = open(FileName, "r")
    FileLine = File.readline()
    String += FileLine
    val_line = 1
    while 1:
        FileLine = File.readline()
        if not FileLine:
            break

        val_line += 1
        if val_line == 3 or val_line == 4 or val_line == 5:
            if curr_sys == "Dos":
                if val_line == 4 or val_line == 5:
                    FileLine = "#" + FileLine
            if curr_sys == "Linux":
                if val_line == 3 or val_line == 5:
                    FileLine = "#" + FileLine
            if curr_sys == "Darwin":
                if val_line == 3 or val_line == 4:
                    FileLine = "#" + FileLine
        String += FileLine

    File.close()
    os.system("rm -rf makefile_pre")

    time.sleep(1)

    FileName = "makefile"
    File = open(FileName, "w")
    File.write(String)
    File.close()





    os.system("clear")
    os.system("rm -rf init.py")
    print("Latex initial finished")
        

if __name__ == '__main__':
    main()

