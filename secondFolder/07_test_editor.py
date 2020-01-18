# Question : Implement a Text Line Editor which supports the following operations:
# insert a line at a given line number
# delete the specific set of lines
# Copy specific set of lines
# Paste the copied lines at given index
# Print the entire content
# display() - to display the entire content
# display(n, m) - to display from line n to m
# insert(n, text) - to insert text at line n
# delete(n) - delete line n
# delete(n, m) - delete from line n to m
# copy(n, m) - copy contents from line n to m to clipboard
# paste(n) - paste contents from clipboard to line n
# undo() - undo last command
# redo() - redo last command

# Commands:
# :q (quit)
# :l (line count)
# :r (read all)
# :r 2 (read specific line)
# :r 2 4 (read line range)
# :i (append at end of file)
# :i 2 (insert at specified line)
# :b (quit from insert mode)
# :d 2 (delete specified line)
# :d 2 4 (delete specified line range)
# :c 2 (copy specified line to clipboard)
# :c 2 4 (copy specified line range to clipboard)
# :p (paste clipboard lines at end of file)
# :p 7 (paste clipboard lines at the specified line)

import os
import sys
import subprocess as sp

root = None
filename = ''
fp = None
lineCount = 0
MODE = {0: 'Command Mode', 1: 'Insert Mode', 2: "Delete Mode"}
currentMode = 0
insertCursor = 0
clipBoard = []


class Node:
    def __init__(self):
        self.line = None
        self.nextNode = None
        self.prevNode = None

    def setLine(self, line):
        self.line = line

    def getLine(self):
        return self.line

    def append(self, line):
        if self.line is None:
            self.setLine(line)
        elif self.nextNode is not None:
            self.nextNode.append(line)
        else:
            newNode = Node()
            if line[-1] != '\n':
                line += '\n'
            newNode.setLine(line)
            newNode.setPrevNode(self)
            self.setNextNode(newNode)

    def insertAt(self, line, lineNo):
        if lineNo == 1:
            newNode = Node()
            newNode.append(line)
            newNode.setNextNode(self)
            newNode.setPrevNode(self.prevNode)

            # prevNode = self.prevNode
            # if prevNode is not None:
            #     prevNode.setNextNode(newNode)
            self.setPrevNode(newNode)

            return newNode
        else:
            self.nextNode = self.nextNode.insertAt(line, lineNo - 1)
            return self
            # if self.prevNode is not None:

    def display(self):
        if self.line is not None:
            sys.stdout.write(self.line)
        if self.nextNode is not None:
            self.nextNode.display()

    def setPrevNode(self, node):
        self.prevNode = node

    def setNextNode(self, node):
        self.nextNode = node

    def getNextNode(self):
        return self.nextNode


def remove(root, start, end):
    global lineCount
    temp = root
    firstNode = None
    secondNode = root

    if start != 1:
        for i in xrange(start - 2):
            temp = temp.getNextNode()
        firstNode = temp
        secondNode = firstNode.getNextNode()

    for i in xrange(end - start + 1):
        temp = secondNode.getNextNode()
        del secondNode
        lineCount -= 1
        secondNode = temp

    if firstNode is not None:
        firstNode.setNextNode(secondNode)
    if secondNode is not None:
        secondNode.setPrevNode(firstNode)

    if start == 1:
        if secondNode is None:
            return Node()
        return secondNode

    return root


def processCommands(text):
    global currentMode, lineCount, insertCursor, root, clipBoard
    commands = ['q', 'r', 'i', 'b', 'd', 'l', 'c', 'p']
    texts = text.split(' ')
    command = texts[0]
    if command not in commands:
        print "**** Not a valid command ****"
    if (currentMode is not 0) and (command not in ['b', 'q']):
        print "**** Please enter command mode ****"
        return
    if command == 'q':
        fp.close()
        sys.exit()
    elif command == 'r':
        if len(texts) == 1:
            root.display()
            return

        start, end = checkRange(texts)
        if start is None:
            return
        copyToClipBoard(root, start, end, 1)

    elif command == 'i':
        # insert
        insertCursor = checkInsertRange(texts)
        if insertCursor is None:
            return
        currentMode = 1
        print "**** Now in Insert Mode ****"
    elif command == 'b':
        # command
        currentMode = 0
        insertCursor = 0
        print "**** Now in Command Mode ****"
    elif command == 'd':
        # currentMode = 2
        # insertCursor = 0
        # print "**** Now in Delete Mode ****"
        start, end = checkRange(texts)
        if start is None:
            return
        root = remove(root, start, end)

    elif command == 'l':
        print lineCount
    elif command == 'c':
        start, end = checkRange(texts)
        if start is None:
            return
        copyToClipBoard(root, start, end, 0)

    elif command == 'p':
        if len(clipBoard) == 0:
            print "**** Clipboard is empty ****"
            return
        insertCursor = checkInsertRange(texts)
        if insertCursor is None:
            return
        for line in clipBoard:
            insertLine(line)
        insertCursor = 0


def checkRange(texts):
    if len(texts) == 1:
        print "**** Please specify range ****"
        return None, None
    start = int(texts[1])
    end = -1
    if len(texts) == 3:
        end = int(texts[2])
    elif len(texts) == 2:
        end = start

    if start > end or end > lineCount:
        print "**** Input range is incorrect ****"
        return None,None

    return start,end


def checkInsertRange(texts):
    if len(texts) == 2:
        currorLine = int(texts[1])
        if currorLine > lineCount:
            print "**** Cannot insert at specified line ****"
            return None
        else:
            insertCursor = currorLine
    else:
        insertCursor = lineCount + 1

    return insertCursor


def copyToClipBoard(root, start, end, mode):
    global clipBoard
    temp = root
    secondNode = root

    if start != 1:
        for i in xrange(start - 2):
            temp = temp.getNextNode()
        secondNode = temp.getNextNode()

    if mode == 0:
        clipBoard = []

    for i in xrange(end - start + 1):
        if mode == 0:
            clipBoard.append(secondNode.getLine())
        elif mode == 1:
            sys.stdout.write(secondNode.getLine())
        temp = secondNode.getNextNode()
        secondNode = temp


def openFile():
    global fp, lineCount
    if os.path.exists(filename):
        fp = open(filename, 'ab+')
        try:
            while True:
                line = fp.readline()
                if line == '':
                    break
                root.append(line)
                lineCount += 1
        except EOFError:
            pass
    fp.close()


def insertLine(line):
    global root, currentMode, lineCount, insertCursor
    if insertCursor == lineCount + 1:
        # print "append"
        root.append(line)
    else:
        root = root.insertAt(line, insertCursor)
    insertCursor += 1
    lineCount += 1


def processText(line):
    # insert
    if currentMode == 1:
        insertLine(line + '\n')


if __name__ == "__main__":
    sp.call('clear', shell=True)
    print "********** Welcome to new text editor **********"
    root = Node()
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        openFile()

    while True:
        try:
            line = raw_input()
            line = line.rstrip(' ')
            if line[0] == ':':
                processCommands(line[1:])
            else:
                processText(line)
        except KeyboardInterrupt:
            sys.exit()
