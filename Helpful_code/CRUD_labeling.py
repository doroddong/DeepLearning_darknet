import os
import sys


def decideRange(range):
    rangeList = range.split('~')
    start = rangeList[0]
    end = rangeList[1]
    return start, end


def checkRange(start, end):
    print(" %s ~ %s, is right?? (if right, write 'ok') : " %
          (start, end), end='')
    i = input("")
    if i == 'ok':
        pass
    else:
        print("Range error")
        sys.exit()


def insertAll(txt_folder, coordinate):
    dirs = os.listdir(txt_folder)
    for x in os.listdir(txt_folder):
        print(x)
        if x.endswith('txt'):
            textFile = open(txt_folder+'/'+x, 'a+')

            textFile.write(coordinate+"\n")
            textFile.close()


def insert(txt_folder, coordinate, start, end):
    dirs = os.listdir(txt_folder)

    for raw in os.listdir(txt_folder):
        temp2 = raw[-7:-4]

        if raw.endswith('txt') and temp2 >= start and temp2 <= end:
            textFile = open(txt_folder+'/'+raw, 'a+')

            textFile.write(coordinate+"\n")
            textFile.close()


def replaceAll(txt_folder, findIndex, replaceIndex):
    dirs = os.listdir(txt_folder)
    for x in os.listdir(txt_folder):
        if x.endswith('txt'):
            textFile = open(txt_folder+'/'+x, 'r')
            lines = textFile.readlines()
            textFile.close()

            if len(lines) != 0:
                textFile_new = open(txt_folder+'/'+x, 'w+')
                for line in lines:
                    line_split = line.split(' ')

                    if line_split[0] == findIndex:
                        line_split[0] = replaceIndex
                        new_line = ''
                        count = 0
                        for i in line_split:
                            new_line += i
                            if count < 4:
                                new_line = new_line+' '
                            count += 1
                        textFile_new.write(new_line)
                    else:
                        textFile_new.write(line)
                textFile_new.close()


def addIndexOne_All(txt_folder):
    dirs = os.listdir(txt_folder)
    for x in os.listdir(txt_folder):
        if x.endswith('txt'):
            textFile = open(txt_folder+'/'+x, 'r')
            lines = textFile.readlines()
            textFile.close()

            if len(lines) != 0:
                textFile_new = open(txt_folder+'/'+x, 'w+')
                for line in lines:
                    line_split = line.split(' ')
                    temp = int(line_split[0])
                    temp = temp+1
                    line_split[0] = str(temp)
                    new_line = ''
                    count = 0
                    for i in line_split:
                        new_line += i
                        if count < 4:
                            new_line = new_line+' '
                        count += 1
                    textFile_new.write(new_line)

                textFile_new.close()


def minusAllIndex(txt_folder):
    dirs = os.listdir(txt_folder)
    for x in os.listdir(txt_folder):
        if x.endswith('txt'):
            textFile = open(txt_folder+'/'+x, 'r')
            lines = textFile.readlines()
            textFile.close()

            if len(lines) != 0:
                textFile_new = open(txt_folder+'/'+x, 'w+')
                for line in lines:
                    line_split = line.split(' ')
                    temp = int(line_split[0])
                    if temp != 0:
                        temp = temp-1
                        line_split[0] = str(temp)
                        new_line = ''
                        count = 0
                        for i in line_split:
                            new_line += i
                            if count < 4:
                                new_line = new_line+' '
                            count += 1
                        textFile_new.write(new_line)
                    else:
                        new_line = ''
                        textFile_new.write(new_line)
                textFile_new.close()


def replaceSub(txt_folder, findIndex, replaceIndex):
    dirs = os.listdir(txt_folder)
    for raw in os.listdir(txt_folder):
        temp2 = raw[-7:-4]

        if raw.endswith('txt') and temp2 >= start and temp2 <= end:
            textFile = open(txt_folder+'/'+raw, 'r')
            lines = textFile.readlines()
            textFile.close()

            if len(lines) != 0:
                textFile_new = open(txt_folder+'/'+raw, 'w+')
                for line in lines:
                    line_split = line.split(' ')

                    if line_split[0] == findIndex:
                        line_split[0] = replaceIndex
                        new_line = ''
                        count = 0
                        for i in line_split:
                            new_line += i
                            if count < 4:
                                new_line = new_line+' '
                            count += 1
                        textFile_new.write(new_line)
                    else:
                        textFile_new.write(line)
                textFile_new.close()
            textFile.close()

argvsize = 2
if len(sys.argv) < argvsize:
    print("usage : python mine.py txt_folder")
else:
    txt_folder = sys.argv[1]
    range = input(
        "Enter range of textFiles ( '.' means all files, and write like 'xxx~yyy')  :  ")

    if(len(range) < 3 and range != '.'):
       print("Write more 3 ")
    else:
        operation = input("Enter operation : " +
                          "  1. Enter Coordinate  " +
                          "  2. Replace index  " +
                          "  3. all index +1   " +
                          "  4. minus all index (-1)  "
                          )
        if(operation == '1'):
            coordinate = input("Write input string? :  ")
            if(range == '.'):
                insertAll(txt_folder, coordinate)
            else:
                start, end = decideRange(range)
                checkRange(start, end)
                insert(txt_folder, coordinate, start, end)

        if(operation == '2'):
            findIndex = input("from which index? :  ")
            replaceIndex = input("to which index? : ")

            if(range == '.'):
                replaceAll(txt_folder, findIndex, replaceIndex)
            else:
                start, end = decideRange(range)
                checkRange(start, end)
                replaceSub(txt_folder, findIndex, replaceIndex)
        if(operation == '3'):
            if(range == '.'):
                addIndexOne_All(txt_folder)
        if(operation == '4'):
            if(range == '.'):
                minusAllIndex(txt_folder)
        else:
            exit()
