import cv2
img = cv2.imread("img2.jpg")

grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Color to  gray scale

cv2.imwrite("grayimg.jpg",grayimg)

cv2.imgshow("orgi",img)

cv2.imgshow("Gray.jpg",grayimg)
cv2.waitKey(0)

cv2.destroyAllWindows