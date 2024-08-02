import cv2 as cv
img=cv.imread("x.png",1)

cv.circle(img,(350,350),300,(160,160,160),15)
cv.line(img,(350,350),(350,55),(160,160,160),30)
cv.line(img,(350,350),(80,450),(160,160,160),30)
cv.line(img,(350,350),(615,450),(160,160,160),30)
cv.imshow("img",img)
cv.waitKey(0)