import cv2
import numpy as np

image = cv2.imread('kaban.jpg')
im = cv2.imread('brigada.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold_level = 50


coords = np.column_stack(np.where(gray < threshold_level))

print(coords)

mask = gray < threshold_level


im[mask] = (200, 100, 0)

cv2.imshow('image', im)
cv2.waitKey()
cv2.imwrite('brigada_kabanov.jpg', im)