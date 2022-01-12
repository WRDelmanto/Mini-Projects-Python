import cv2
import numpy as np

path = "test1.png"
blur_value = 5
line_thickness = 5
k = 9

# Read File
img = cv2.imread(path)

# Create Edge Mask
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blur = cv2.medianBlur(gray, blur_value)
edges = cv2.adaptiveThreshold(
    gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_thickness, blur_value)

# Transform the Image
data = np.float32(img).reshape((-1, 3))

# Determine Criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

# Implementing K-Means
ret, label, center = cv2.kmeans(
    data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
center = np.uint8(center)
cartoon = center[label.flatten()]
cartoon = cartoon.reshape(img.shape)

# Bilateral Filter
blurred = cv2.bilateralFilter(img, d=7, sigmaColor=200, sigmaSpace=200)

# Combine Edge Mask with the Colored Image
cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)

# cv2.imshow("Image", img)
# cv2.imshow("Edges", edges)
cv2.imshow("Cartoon", cartoon)

cv2.waitKey(0)
cv2.destroyAllWindows()
