import os
LINE_LIMIT = 99

def getFilenameList():
    filenameList = []
    for dirName in os.listdir('.'):
        if dirName[0] != '.' and os.path.isdir('./' + dirName):
            dirPath = './' + dirName
            for filename in os.listdir(dirPath):
                filePathName = dirPath + '/' + filename
                if '.py' in filePathName:
                    filenameList.append(filePathName)

    return filenameList


def formatLine(resStr):
    resStr = resStr.replace('\n', ' ')
    thisLineLimit = LINE_LIMIT
    while len(resStr) > thisLineLimit:
        spaceChar = thisLineLimit
        while resStr[spaceChar] != ' ':
            spaceChar -= 1
        print spaceChar
        resStr = resStr[:spaceChar] + '\n' + resStr[spaceChar+1:]
        thisLineLimit += LINE_LIMIT
    return resStr


def readFileName():
    f = open("fileList.txt")
    lines = list(f)
    lines = [line[:-1] for line in lines]
    return lines


def getQuestion(filename, count, resOutputFile):

    fp = open(filename, 'r')
    resStr = ''
    while True:
        line = fp.readline()
        if not line:
            break

        if '# Question :' in line:
            while len(line.replace('#', '')) >= 2:
                line = line.replace('# ', '')
                resStr += line
                line = fp.readline()
            break
    if len(resStr) >= 1:
        # resStr = formatLine(resStr)
        resOutputFile.write(str(count[0]) + '. Filename : ' + filename + '\n')
        resOutputFile.write(resStr + '\n')
        count[0] += 1
    else:
        print "Question not found: ", filename
    fp.close()


if __name__ == "__main__":
    filenameList = getFilenameList()
    #filenameList = readFileName()
    #filenameList = ['01_array/32_zero_matrix.py']
    count = [1]
    resOutputFile = open('all_questions.txt', 'w')
    for filename in filenameList:
        getQuestion(filename, count, resOutputFile)
    print count[0]
    resOutputFile.close()


