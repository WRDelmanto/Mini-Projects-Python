from PIL import Image

filename = "Image.png"

img_file = Image.open(filename)

width = img_file.size[0]
height = img_file.size[1]

print(width, height)
