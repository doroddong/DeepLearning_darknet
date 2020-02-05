import os,sys
import re

def openDir(path):     
    dirs = os.listdir(path)

    return dirs

def replaceName(files,name):                                                                       
    for file in files:
        if file.endswith(".jpg"):
            number = re.findall('\d+',file)
            new_filename = name + number[0]+'.jpg'
            os.rename(path+'/'+file,path+'/'+new_filename)

def addFront(files,name):
    for file in files:
        if file.endswith(".jpg"):
            new_filename = name + file
            os.rename(path+'/'+file,path+'/'+new_filename)

def addExtension(files):
    for file in files:
        new_filename = file + '.jpg'
        os.rename(path+'/'+file,path+'/'+new_filename)

argvsize=3
if len(sys.argv) < argvsize:
    print("usage : python rename.py path Name")
else:
    path = sys.argv[1]
    name = sys.argv[2]
    
    function = input("1. Add at front  2. Replace name  3. Add extension =>  ")  # Select operation

    files = openDir(sys.argv[1])
    
    if function == '1' :
        addFront(files,name)
    elif function == '2':
        replaceName(files,name)
    elif function == '3':
        addExtension(files)
    else :
        print("No operation")
        exit()