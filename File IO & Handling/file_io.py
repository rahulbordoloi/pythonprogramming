# File Objects

import os

## Read Files
# Using Context Manager
with open('test.txt', 'r') as f: 
    pass
    # contents = f.read()
    #contents = f.readlines()
    '''
    contents = f.readline()
    print(contents, end = '')
    contents = f.readline()
    print(contents, end = '')
    '''
    # for line in f:
    #    print(line, end = '')
    
    '''
    size_to_read = 10
    f_content = f.read(size_to_read)
    while len(f_content) > 0:
        print(f_content, end = '*')
        f_content = f.read(size_to_read)
    '''

    # f.seek(0)     # To point our file pointer to that particular location

## Write Files
with open('test_w.txt', 'w') as f:
    pass
    # f.write("Hello World")
    # f.seek(0)
    # f.write("Rahul")

## Copying Files

### Text Files
'''
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

## Large - Image Files
with open('_MG_8632.jpg', 'rb') as rf:
    with open('rony_copy.jpg', 'wb') as wf:
        chunk_size = 4096                   # Defining Chunks
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
'''

## Deleting Files
path = './bye.txt'
print(os.path.isfile(path))
try:
    if os.path.isfile(path):
        os.remove(path)
except:
    print(f'Error : {path} - invalid path defined')
print(os.path.isfile(path))
