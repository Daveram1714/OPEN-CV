import cv2
img = cv2.imread('img2.jpg')

gaussianBlur = cv2.GaussianBlur(img,(25,25),0)

cv2.imwrite("Blur.jpg",gaussianBlur)