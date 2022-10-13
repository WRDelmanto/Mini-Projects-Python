from rembg import remove
from PIL import Image

path = "test.png"

img = Image.open(path)

img_without_back = remove(img)

img_without_back.save("test1.png")
