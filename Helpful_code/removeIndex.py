import os,sys

def change(txt_folder, removeNumber):    
    
    dirs = os.listdir(txt_folder)
    for item in dirs:    
        
        fileName, fileExtension = os.path.splitext(item)
        
        if fileExtension == '.txt':
            txtFile = open(txt_folder + '/' + item, 'r')
            lines = txtFile.readlines()
            txtFile.close()
            
            if len(lines) != 0:
                
                txtFile_new = open(txt_folder + '/' + item, 'w')
                
                for line in lines:
                    
                    line_split = line.split(' ')
                    number = line_split[0]
                    if (number == removeNumber):
                        line = ""
                    txtFile_new.write(line)
                txtFile_new.close()
                
def main(argv):
    
    txt_folder = argv[0]
    number = argv[1]
    change(txt_folder, number)

argvsize = 3
if len(sys.argv) < argvsize:
    print("usage : python removeIndex.py txt_folder number")
else:
    main(sys.argv[1:])