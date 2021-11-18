import os
from categoryWise import questionMap
fileName = "allFilesComments_category2.txt"


def fetchFile(qFile):
    comments = []
    with open(qFile + '.py', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("#"):
                if len(line) == 2:
                    comments.append("\n")
                else:
                    comments.append(line[2:])
            else:
                break
    return ''.join(comments)


def writeInFile(qFile, category, comments, count):
    with open(fileName, 'a+') as f:
        f.write("Category : " + category + "\n")
        f.write(str(count) + ". " + qFile + "\n\n")
        f.write(comments)
        f.write("\n")
        f.write("****************************************************************")
        f.write("\n\n")

def extract_comment():
    count = 0
    for category, qList in questionMap.items():
        for qFile in qList:
            comments = fetchFile(qFile)
            count += 1
            writeInFile(qFile, category, comments, count)

    print (count)


if __name__ == "__main__":
    if os.path.exists(fileName):
        os.remove(fileName)
    extract_comment()
