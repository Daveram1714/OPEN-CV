import cv2
img = cv2.imread("img2.jpg")

grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

threshimg = cv2.threshold(grayimg,190,255,cv2.THRESH_BINARY)[1]  #applied the threshold

cv2.imwrite("DIGITAL IMG.jpg",threshimg)