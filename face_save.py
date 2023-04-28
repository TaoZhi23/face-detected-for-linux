#导入cv模块
import cv2
import numpy as np
import os

# 获取当前已经保存的人脸数
path='./data/face/'
num = len(os.listdir(path=path))
# 新识别的人脸编号
num = num+1

def is_single_face(rec):
    '''
    输入获取的face矩形数据，返回是否检测到。
    有脸且只有一张，返回将rec降维后生成的list
    否则返回None
    '''
    if str(type(rec)) != "<class 'numpy.ndarray'>":
        return None
    # print(type(rec))
    a = rec.reshape(1, -1).ravel().tolist()
    # print('a=',a)
    if len(a) != 4:
        return None
    return a

#检测函数
def face_detect_demo(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_detect = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt2.xml')
    rec = face_detect.detectMultiScale(gray,1.1,5,cv2.CASCADE_SCALE_IMAGE,(100,100),(300,300))
    # for x, y, w, h in rec:
    #     print("numpy: ", x, y, w, h)
    #     cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    return img, rec

def save_face(rec, face):
    '''
    输入矩形数组，图片
    保存脸部图片到路径“./data/face/”
    '''
    x, y, w, h = rec
    f = face[y-h//8:y+h+h//8, x-w//8:x+w+w//8]
    cv2.putText(face, 'if you confirm, press s to input your name',
                (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
    cv2.putText(face, 'if not, press q to quit', (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
    cv2.imshow('face', f)
    cv2.imshow('original', face)
    if cv2.waitKey(0) == ord('s'):
        cv2.destroyAllWindows()
        # 输入名字，然后保存图片
        name = input("prees your name: ")
        if cv2.imwrite("./data/face/"+str(num)+"."+name+".png", f):
            print("finished")
        else:
            print('failed to save face')


if __name__ == '__main__':
    # 初始化
    face = None
    face_rec = None
    # 调用本地摄像头
    cap = cv2.VideoCapture(0)
    # 主循环
    while cap.isOpened():
        ret, frame = cap.read()
        # 获取图片成功则执行
        if ret:
            # 图像左右翻转写1，上下翻转写0,180度写-1
            cv2.flip(frame, 1, frame)
            frame, rec = face_detect_demo(frame)
            show = frame.copy()
            for x, y, w, h in rec:
                cv2.rectangle(show, (x,y), (x+w,y+h), color=(0,0,255), thickness=2)
            cv2.putText(show, 'press q to quit',(10, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            cv2.putText(show, 'press s to save face when only one rectangle',(10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            cv2.imshow('capture', show)
        # 等待键盘输入
        if cv2.waitKey(20) == ord('q'): # 输入q，退出程序
            print('exit program')
            cv2.destroyAllWindows()
            exit()
        elif cv2.waitKey(20) == ord('s'): # 输入s，开始保存图片
            face_rec = rec
            face = frame
            cv2.destroyWindow('capture')
            break
    cap.release()
    # 判断脸型矩阵并获得对应数组
    rec_list = is_single_face(rec=face_rec)
    # 获取成功
    if rec_list != None:
        # print('successfully')
        save_face(rec_list, face)
    # 获取失败
    else:
        print('failed')
    cv2.destroyAllWindows()
    exit()