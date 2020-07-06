import os

# Path 
path = "C:/Users/KIIT/Desktop"
  
# Path of Start directory 
start = "C:/User/KIIT/Downloads"
  
# Compute the relative file path to the given path from the the given start directory. 
relative_path = os.path.relpath(path, start) 
  
# Print the relative file path to the given path from the the given start directory. 
print(relative_path) 
