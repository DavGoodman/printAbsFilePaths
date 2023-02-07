import os
# Finds and prints the abs paths of all files in a folder and sub folder.
# Can be expanded for other uses besides printing
num = 0
for foldername, subfolders, filenames in os.walk(folder_path):
    num += 1
    path = folder_path
    for filename in filenames:
        if num >= 1:
            path = folder_path / foldername
            print(path / filename)

        else:
            print(path / filename)