import cv2 as cv
img = cv.imread("new-features-B.jpg")

#修改尺寸
resize_img = cv.resize(img, dsize = (200,200))
#显示原图
cv.imshow('resize_img', resize_img)
#显示修改后的
print("未修改", img.shape)
#打印原图尺寸大小
print("已修改", resize_img.shape)

while True:
    if ord('q')==cv.waitKey(0):
        break

#释放内存
cv.destroyAllWindows()