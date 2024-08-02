import cv2 as cv
img=cv.imread("x.png",1)

cv.circle(img,(350,300),50,(0,0,0),5)
cv.circle(img,(460,300),50,(0,0,255),5)
cv.circle(img,(240,300),50,(255,0,0),5)
cv.circle(img,(295,345),50,(0,255,255),5)
cv.circle(img,(405,345),50,(0,255,0),5)

cv.imshow("img",img)
cv.waitKey(0)