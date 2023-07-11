import os
from categoryWise import questionMap as catQuestionMap
from top_125 import questionMap as topQuestionMap
fileName_cat = "allFilesComments_category.txt"
fileName_top = "allFilesComments_top_125.txt"


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


def extract_comment(questionMap):
    count = 0
    for category, qSet in questionMap.items():
        qList = list(qSet)
        qList.sort()
        fCount = 0
        print(category)
        for qFile in qList:
            comments = fetchFile(qFile)
            count += 1
            fCount += 1
            categoryLabel = category + ' (%s of %s)' % (fCount, len(qList))
            writeInFile(qFile, categoryLabel, comments, count)

    print(count)


if __name__ == "__main__":
    questionMap = topQuestionMap
    fileName = fileName_top

    if os.path.exists(fileName):
        os.remove(fileName)
    extract_comment(questionMap)
