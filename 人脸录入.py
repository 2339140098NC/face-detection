import cv2

#读取摄像头
cap = cv2.VideoCapture(0)

falg = 1
num = 1

while(cap.isOpened()):#检测摄像头开启状态
    ret_flag, Vshow = cap.read()#读取图像
    cv2.imshow('Capture_test', Vshow)#显示图像
    k = cv2.waitKey(1) & 0xFF # 案件判断
    if k == ord('s'):#保存
        cv2.imwrite("D:/opencv/trainer/faces/" + str(num) + ".name" + ".jpg" , Vshow)
        print("success to save " + str(num) + ".jpg")
        print("----------")
        num += 1
    elif k == ord(" "):
        break

#释放摄像头
cap.release()
#释放内存
cv2.destroyAllWindows()