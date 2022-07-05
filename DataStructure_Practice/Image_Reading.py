import cv2
import pytesseract

img = cv2.imread("/Users/arvin/downloads/1.png")

text = pytesseract.image_to_string(img)
print(text)