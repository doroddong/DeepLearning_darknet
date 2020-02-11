import os,sys,shutil

def mkdir(dir_path):
    dirs = os.listdir(dir_path)
    print(dirs)
    for x in dirs:
        if os.path.isfile(dir_path+"\\"+x):
            filename=x.split('.')[0]
            print(filename)
            if os.path.isdir(dir_path+"\\"+filename)==0:
                os.mkdir(dir_path+"\\"+filename+"\\")
            shutil.move(dir_path+"\\"+x,dir_path+"\\"+filename+"\\"+x)


argvsize=2

if len(sys.argv)<argvsize:
    print("usage : python mkdir.py dir_path")
else:
    dir_path =sys.argv[1]
    mkdir(dir_path)