import os,sys,subprocess

def runConvert(listfile):
    print(os.getcwd())
    print(listfile)
    pwd =os.getcwd()
    listFile = open(pwd+'/'+listfile,'r')
    lines = listFile.readlines()
    listFile.close()

    if len(lines)!=0:
        for line in lines:
            print(line)
            subprocess.SW_HIDE=1
            
            os.chdir("video")
            r= subprocess.run(["youtube-dl",line],capture_output=True)
            print(r)

argvsize=2
if len(sys.argv) < argvsize:
    print("usage : python youtube.py linkList.txt")

else:
    listfile=sys.argv[1]
    print(listfile)
    runConvert(listfile)