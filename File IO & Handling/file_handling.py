# Importing Libraries
import os
import fnmatch
import glob

## Check if a File Exists using Assert-OS Module
assert os.path.isfile('test.txt'), "File Doesn't Exist"
assert os.path.isdir('Temp'), "Directory Doesn't Exist"
# assert os.path.isfile('rahul.txt'), "File Doesn't Exist"

## Check if a File Exists using Try-Catch
'''
try:
    f = open('myfile.txt')
    f.close()
except FileNotFoundError:
    print('File does not Exist!')
'''

# print(os.listdir())          # Lists all the File/Sub Dirs present in the CWD in a List

## Search Operation if a File Ends with .txt
'''
c = 0
for file in os.listdir():
    if file.endswith(".txt"):
        print(file)
        c += 1
print(c)
'''

## Advanced Searching File Names with fnmatch()
'''
for file in os.listdir():
    if fnmatch.fnmatch(file, '*temp*'):
        print(file)
'''

## Advanced Searching File Names with glob() and iglob()
# glob() returns a list
# iglob() returns an iterator
# resersive = True prompts to search for files in sub-dirs too
# * - Only CWD
# ** - CWD + All Sub-Dirs
'''
for name in glob.glob('*_*', recursive = True):
    print(name)

for file in glob.iglob('**/*.txt', recursive = True):     
    print(file)
'''

## Display all the Files and Folders of Current CWD
for dirpath, dirnames, files in os.walk('.', topdown = False):
    print(f'Directory Found : {dirpath}')
    for file in files:
        print(file)




