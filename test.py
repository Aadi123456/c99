import os
import shutil

# Write the name of the directory here,
# that needs to get sorted
# path = '/home/rajeev/Videos'
path = input("enter the name of the directory to be sorted :- ")

# This will create a properly organized
# list with all the filename that is
# there in the directory
list_of_files = os.listdir(path)

# This will go through each and every file
for file in list_of_files:
    name, ext = os.path.splitext(file)
    print('name',name)
    print('ext', ext)
    # This is going to store the extension type
    ext = ext[1:]
    print('ext[1:]',ext)