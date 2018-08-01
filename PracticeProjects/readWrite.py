#readWrite.py
#Functions for checking if a file exists, read from a file, write to  a file

import os
def fileExists(filepath):
     exists = os.path.exists(filepath)
     return exists

def writeFile(filepath, txtToWrite):
    fileHandle = open(filepath, 'w')
    fileHandle.write(txtToWrite)
    fileHandle.close()

def readFile(filepath):
    if not fileExists(filepath):
        print "file does not exist"
        return ''
    fileHandle = open(filepath, 'r')
    data = fileHandle.read()
    fileHandle.close()
    return data

file = 'log.txt'
string = 'this is new string and another one'
writeFile(file, string)
print readFile(file)
