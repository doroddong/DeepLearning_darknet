import sys,os,subprocess

def executeFFmpeg(dir_path):
    dirs = os.listdir(dir_path)
    for x in dirs:
        inner_path=dir_path+"\\"+x
        
        if os.path.isdir(inner_path):
            dirs_inner=os.listdir(inner_path)
            for y in dirs_inner:
                # only video file
                if y.endswith('mp4') or y.endswith('mkv') or y.endswith('webm'):
                    
                    # C:/Users/dmlee-nb01/Desktop/dong/youtube-dl/bin/ffmpeg.exe -i some_path/y+' -r 10 -f image2 some_path_%d.jpg 
                    
                    command ='C:\\Users\\dmlee-nb01\\Desktop\\dong\\youtube-dl\\bin\\ffmpeg.exe -i '+inner_path+"\\"+y+' -r 10 -f image2 '+inner_path+"\\"+x+'_%d.jpg'

                    p=subprocess.Popen(command)
                    (output,err) = p.communicate()
                    p_status=p.wait()
                    
                    #print(output)
                    #print(err)
    print("Done!!")



argvsize=2
if len(sys.argv)<argvsize:
    print("usage : python excuteFFmpeg.py dir_path")
else:
    dir_path = sys.argv[1]
    executeFFmpeg(dir_path)