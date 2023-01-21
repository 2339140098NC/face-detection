import cv2 as cv

def face_detect_demo():
    gary = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier('D:/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
    face = face_detect.detectMultiScale(gary, 1.01, 8, 0, (40,40),(50,50))
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w, y+h), color=(0,0,255), thickness = 2)
    cv.imshow('result', img)
#读取图像
img = cv.imread("SC1927.jpg")

face_detect_demo()

while True:
    if ord('q')==cv.waitKey(0):
        break
#释放内存
cv.destroyAllWindows()