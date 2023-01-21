import cv2 as cv

img = cv.imread("new-features-B.jpg")
#灰度转换
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#显示灰度
cv.imshow('gray',gray_img)
#保存灰度图片
cv.imwrite('gray_face11.jpg', gray_img)


#显示图片
cv.imshow('read_img', img)
#等待
cv.waitKey(0)
#释放内存
cv.destroyAllWindows()