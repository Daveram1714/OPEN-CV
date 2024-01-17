import cv2
img = cv2.imread("img2.jpg")  #Read an image
cv2.imwrite("newlogo.png",img) #wirte an image
cv2.imshow("PS LOGO",img)# display the image untill close
cv2.waitKey(0)

cv2.destroyWindow(0)