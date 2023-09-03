import os
from top_200 import questionMap as topQuestionMap
from category_wise import questionMap as CategoryQuestionMap

fileName_category = "comments_category.txt"
fileName_top = "comments_top_200.txt"
fileName_to_note = "comments_to_note.txt"
fileName_remaining = "comments_remaining.txt"


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
        print(category, len(qList))
        for qFile in qList:
            comments = fetchFile(qFile)
            count += 1
            fCount += 1
            categoryLabel = category + ' (%s of %s)' % (fCount, len(qList))
            writeInFile(qFile, categoryLabel, comments, count)

    print(count)


def get_all_filename_list():
    ignore_folders = ['utility', 'assignment']
    filename_list = []
    for dirName in os.listdir('.'):
        if dirName[0] != '.' and dirName not in ignore_folders and os.path.isdir('./' + dirName):
            dirPath = './' + dirName
            for filename in os.listdir(dirPath):
                if '00' in filename:
                    continue
                filePathName = dirPath + '/' + filename
                if '.py' in filePathName and '.pyc' not in filePathName:
                    replaced = filePathName.replace(".py", "")
                    replaced = replaced.replace("./", "")
                    filename_list.append(replaced)

    return sorted(filename_list)


def get_remaining_questions(question_map):
    top_questions = []
    for value in question_map.values():
        top_questions.extend(value)

    not_included = list(sorted(set(get_all_filename_list()) - set(top_questions)))
    new_question_map = dict()
    new_question_map["Remaining"] = not_included
    return new_question_map


def make_md_file(question_map, file_name='sample.md'):
    f = open(file_name, 'w+')
    for key, values in question_map.items():
        f.write("\n\n## " + key + "\n\n")

        count = 0
        for item in sorted(list(values)):
            count += 1
            f.write(str(count) + ". " + "[" + item + "]" + "(" + item + ".py" + ")\n")

    f.close()


if __name__ == "__main__":
    # Extract category questions
    # question_map = CategoryQuestionMap
    # fileName = fileName_category
    # if os.path.exists(fileName):
    #     os.remove(fileName)
    # extract_comment(question_map)

    # Extract top questions
    question_map = topQuestionMap
    make_md_file(topQuestionMap, 'top_questions.md')
    fileName = fileName_top
    if os.path.exists(fileName):
        os.remove(fileName)
    extract_comment(question_map)

    # Extract remaining questions
    new_question_map = get_remaining_questions(question_map)
    make_md_file(new_question_map, 'remaining_questions.md')
    fileName = fileName_remaining
    if os.path.exists(fileName):
        os.remove(fileName)
    extract_comment(new_question_map)
