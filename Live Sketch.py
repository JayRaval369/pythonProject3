
import cv2
import numpy as np

def nothing(X):
    pass

cap=cv2.VideoCapture(0)
cv2.namedWindow('sketch')

cv2.createTrackbar('LTC','sketch',0,255,nothing)
cv2.createTrackbar('UTC','sketch',0,255,nothing)

while True:
    ret,im=cap.read()
    roi=cv2.selectROI("original",im,False,False)
    cv2.destroyAllWindows()
    break

while True:
    ret,frame=cap.read()

    image=frame[int(roi[1]):int(roi[1]+roi[3]),(roi[0]):int(roi[0]+roi[2])]

    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image=cv2.GaussianBlur(image,(7,7),0)

    ltc=cv2.getTrackbarPos('LTC','sketch')
    utc=cv2.getTrackbarPos('UTC','sketch')

    image=cv2.Canny(image,10,60)
    ret,image=cv2.threshold(image,50,255,cv2.THRESH_BINARY_INV)

    image=cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)

    image=frame[int(roi[1]):int(roi[1]+roi[3]),(roi[0]):int(roi[0]+roi[2])]=image

    cv2.imshow("original",frame)
    cv2.imshow("sketch",frame)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
