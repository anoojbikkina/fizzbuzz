os.listdir(path='.')

Python
'''
For the given path, get the List of all files in the directory tree 
'''
def getListOfFiles(dirName):
# create a list of file and sub directories 
# names in the given directory 
listOfFile = os.listdir(dirName)
allFiles = list()
# Iterate over all the entries
for entry in listOfFile:
# Create full path
fullPath = os.path.join(dirName, entry)
# If entry is a directory then get the list of files in this directory 
if os.path.isdir(fullPath):
allFiles = allFiles + getListOfFiles(fullPath)
else:
allFiles.append(fullPath)
return allFiles
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
'''
    For the given path, get the List of all files in the directory tree 
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles



import os
def walk(dirname):
	for name in os.listdir(dirname):
		path = os.path.join(dirname,name)
		if os.path.isfile(path):
			print(path)
		else:
			walk(path)

