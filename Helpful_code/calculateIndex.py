import os,sys

index_list = ['0','1','2','3','4']
index_counter = [0,0,0,0,0]

def calculateIndex(txt_folder):
    dirs = os.listdir(txt_folder)
    for x in dirs:
        if x.endswith('txt'):
            textFile = open(txt_folder+'/'+x,'r+')
            lines = textFile.readlines()
            #print(textFile.name)
            textFile.close()

            if len(lines) !=0:
                for line in lines:
                    line_split = line.split(' ')
                    #print(line)
                    k = line_split[0]
                    #print(k)
                    index_counter[int(k)]+=1
                    #print(index_counter)
    print(index_counter)
                        
argvsize =2
if len(sys.argv) < argvsize:
    print("usage : python calculateIndex.py txt_folder")
else:
    txt_folder = sys.argv[1]
    calculateIndex(txt_folder)