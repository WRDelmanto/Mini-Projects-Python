import os

path = "Test"
oldExtension = ".ts"
newExtension = ".avi"

for root, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith(oldExtension)):
            # print(os.path.join(root, file))
            newFile = file.replace(oldExtension, newExtension)
            os.rename(os.path.join(root, file), os.path.join(root, newFile))
