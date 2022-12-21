import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image

image = cv2.imread("test.png")
string = pytesseract.image_to_string(image)
# печатаем
print(string)
