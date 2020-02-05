import os,sys
from PIL import Image, ImageDraw

def changeformat(yolobox, size):
    
    w, h = size
    
    box_w = float(yolobox[2]) * w
    box_h = float(yolobox[3]) * h
    x1 = int(float(yolobox[0]) * w - box_w/2)
    y1 = int(float(yolobox[1]) * h - box_h/2)
    x2 = int(x1 + box_w)
    y2 = int(y1 + box_h)

    x1 = max(x1, 0)
    x2 = min(x2, w)
    y1 = max(y1, 0)
    y2 = min(y2, h)

    return (x1,y1),(x2,y2)

def checkoverlap1D(line1, line2):
    min1 = line1[0]
    max1 = line1[1]
    min2 = line2[0]
    max2 = line2[1]

    sign = False
    if max1 >= min2 and max2 >= min1:
        sign = True
    
    return sign



def removeMasking(txt_folder):    
    
    dirs = os.listdir(txt_folder)
    for item in dirs:    
        
        fileName, fileExtension = os.path.splitext(item)
        
        if fileExtension == '.txt':
            txtFile = open(txt_folder + '/' + item, 'r')
            lines = txtFile.readlines()
            txtFile.close()

            if len(lines) != 0:

                txtFile_new = open(txt_folder + '/' + item, 'r')
                

                # 마스킹리스트 생성
                maskingList = []
                objectList = []
                for line in lines:
                    
                    line_split = line.split(' ')
                    index = line_split[0]
                    if index == '0':                                      # index가 0인 것만 
                        maskingList.append(line_split[1:])
                    else:
                        objectList.append(line_split[1:])


                # 마스킹영역 삭제 (m: masking, o: object, i: intersection, 1: min, 2: max)
                if len(maskingList) is not 0:
                    
                    im = Image.open(txt_folder + '/' + fileName + '.jpg')
                    draw = ImageDraw.Draw(im)

                    if len(objectList) is 0:
                        for index_masking in maskingList:
                            (mx1, my1), (mx2, my2) = changeformat(index_masking, im.size)
                            draw.rectangle([(mx1, my1), (mx2, my2)], fill="black")
                    else:
                        
                        flag = Image.new("1", im.size) # 바이너리형식의 이미지파일 생성 (초기값은 0)
                        pixels_flag = flag.load()      # 픽셀값 로드

                        for index_masking in maskingList:
                            (mx1, my1), (mx2, my2) = changeformat(index_masking, im.size) # 다크넷형식에서 변환

                            for x in range(mx1, mx2):
                                for y in range(my1, my2):
                                    pixels_flag[x,y] = 1
                        
                        for index_object in objectList:
                            (ox1, oy1), (ox2, oy2) = changeformat(index_object, im.size)

                            for x in range(ox1, ox2):
                                for y in range(oy1, oy2):
                                    pixels_flag[x,y] = 0
                        
                        w,h = im.size
                        pixels_im = im.load()
                        for x in range(w):
                            for y in range(h):
                                if pixels_flag[x,y]:
                                    pixels_im[x,y] = (0,0,0)    # 마스킹영역만 삭제

                                
                    im.save(txt_folder + '/' + fileName + '.jpg')

                txtFile_new.close()


def main(argv):
    
    txt_folder = argv[0]
    removeMasking(txt_folder)



if __name__ == "__main__":
    argvsize = 2
    if len(sys.argv) < argvsize:
        print("usage : python removeMasking.py txt_folder")
    else:
        main(sys.argv[1:])
