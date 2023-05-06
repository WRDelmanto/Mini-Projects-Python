import os


def convertAnyFileInPathImproperWay(path: str, oldExtension: str, newExtension: str):
    # Iterate over all files and directories within the given path
    for root, dirs, files in os.walk(path):
        # Iterate over all files within the current directory
        for file in files:
            # Check if the file ends with the old extension
            if (file.endswith(oldExtension)):
                # Create a new file name with the new extension
                newFile = file.replace(oldExtension, newExtension)
                # Rename the file with the new name and extension
                os.rename(os.path.join(root, file),
                          os.path.join(root, newFile))


convertAnyFileInPathImproperWay("temp", ".mp4", ".avi")
