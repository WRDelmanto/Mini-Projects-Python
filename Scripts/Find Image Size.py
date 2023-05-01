from PIL import Image

filename = "temp.png"

img_file = Image.open(filename)

width = img_file.size[0]
height = img_file.size[1]

print("Width:", width)
print("Height:", height)
