import cv2

alg = "haarcasade_forntalface_default.xml"
haar_cascade = cv2.VideoCapture(0)

cam = cv2.VideoCapture(0)

while True:
    _,img = cam.read()
    grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayimg,1,3,4)

    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+y,y+h),(0,255,0),2)
    cv2.imgshow("FaceDectection",img)
    key = cv2.waitkey(10)
    if key ==27:
        break

cam.release()
cv2.destroyAllWindows()