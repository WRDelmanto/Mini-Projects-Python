import cv2

path = "test.png"

image = cv2.imread(path)
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_image)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedBlur = cv2.bitwise_not(blur)

sketch = cv2.divide(grey_image, invertedBlur, scale=220.0)

cv2.imwrite("Sketch.png", sketch)
