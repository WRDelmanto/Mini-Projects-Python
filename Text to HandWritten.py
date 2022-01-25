import pywhatkit as kit
import cv2

text = "This is a test"
path = "test.png"

kit.text_to_handwriting(text, save_to=path)
img = cv2.imread(path)
cv2.imwrite(path, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
