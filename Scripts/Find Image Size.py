from PIL import Image


def getImageSize(filename):
    # Open the image file
    img_file = Image.open(filename)

    # Extract the width and height of the image
    width = img_file.size[0]
    height = img_file.size[1]

    # Print out the width and height of the image
    print("Width:", width)
    print("Height:", height)


getImageSize("temp.png")
