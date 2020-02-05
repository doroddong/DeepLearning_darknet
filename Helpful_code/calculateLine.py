import os,sys

def calculateLine(txt_folder):
    dirs = os.listdir(txt_folder)
    for x in dirs:
        if x.endswith('txt'):
            textFile = open(txt_folder+'/'+x,'r+')
            lines = textFile.readlines()
            textFile.close()
            if len(lines)>5:
                #print(textFile.name)
                #print(len(lines))
                print(lines)

argvsize =2
if len(sys.argv) < argvsize:
    print("usage : python mine.py txt_folder")
else:
    txt_folder = sys.argv[1]
    calculateLine(txt_folder)