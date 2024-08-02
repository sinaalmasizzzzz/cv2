import cv2 as cv
img=cv.imread("x.png",1)
cv.rectangle(img,(0,0),(700,150),(0,255,0),-1)
cv.rectangle(img,(0,300),(700,150),(255,255,255),-1)
cv.rectangle(img,(0,300),(700,450),(0,0,255),-1)
cv.imshow("img",img)
cv.waitKey(0)