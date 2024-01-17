import cv2
img = cv2.imread("img2.jpg")

graying = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gaussianimg = cv2.GaussianBlur(graying,(21,21),0)

threshold = cv2.threshold(graying,150,255,cv2.THRESH_BINARY)[1]

cv2.imwrite("Threshold.jpg",threshold)