# -*- coding: UTF-8 -*-
import Face as f
import Control as c
import cv2
import time

#Write By ITJoker Time：2018.10.10
#若无法使用，则先 sudo apt-get install fswebcam & sudo apt-get install libv4l-dev

faceflag=0
faceUploadbit=1
def Upload(frame,access_token,group_id_list):
    global faceUploadbit                                                                                                                            #获取全局变量faceUploadbit
    global faceflag                                                                                                                                 #获取全局变量faceflag
    if (!faceUploadbit):                                                                                                                            #判断上传位是否为0
        img=f.open_picture()                                                                                                                        #读取照片并编码为base64
        output=f.FaceSearch (img,access_token,group_id_list)                                                                                        #开始匹配并将反馈信息赋值给output
        flag=f.ReadData(output,70)                                                                                                                  #处理反馈信息并获取是否识别成功标志，相似度判断值默认70
        if (flag):                                                                                                                                  #判断标志是否为1
            c.Open(pin)                                                                                                                             #打开GPIO为pin值的口
            time.sleep(0.5)                                                                                                                         #延时0.5秒
            c.Stop(pin)                                                                                                                             #关闭GPIO为pin值的口
            return 2                                                                                                                                #返回值为2
        else:
            cv2.putText(frame,"Open GPIO Failed!", ( 10, 10 ), cv2.FONT_HERSHEY_SIMPLEX, 0.3, ( 0, 0, 255 ), 1 )                                    #界面上方输出GPIO打开失败
            return 1                                                                                                                                #返回值为1
    else:
        return 0                                                                                                                                    #返回值为0
def Mains():
    #############----Setup Main Config----####################
    ApiKey=""                                                    #从百度AI获取到的ApiKey
    SecretKey=""                                        #从百度AI获取到的SecretKey
    group_id_list="test_1"                                                               #从百度AI获取到的用户组名
    pin=7                                                                                #默认控制GPIO为7
    ##########################################################
    
    #############-----Setup USB Camera Config----#############
    cascPath = "haarcascade_frontalface_default.xml"                                     #训练集文件地址
    faceCascade = cv2.CascadeClassifier(cascPath)                                        #加载人脸检测的训练集
    video_capture = cv2.VideoCapture(0)                                                  #调用默认的usb摄像头
    video_capture .set(cv2.cv.CV_CAP_PROP_FPS ,60)                                       #设置摄像头帧数为60（虽然最大貌似为30但先选为60）
    video_capture .set(3,160)                                                            #设置摄像头分辨率Width为160
    video_capture .set(4,120)                                                            #设置摄像头分辨率Height为120
    ##########################################################
    access_token=f.GetAccess_token(ApiKey,SecretKey)                                     #获取access_token
    if(access_token):                                                                    #判断access_token是否获取成功
        while True:
            global faceUploadbit                                                                                                                            #获取全局变量faceUploadbit
            global faceflag                                                                                                                                 #获取全局变量faceflag
            if(faceUploadbit):                                                                                                                              #判断上传位是否为1，若真，facefalg自加1
                faceflag=faceflag+1
            ret, frame = video_capture.read()                                                                                                               #读取摄像头的第一帧
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                                                                                                  #将图像转化为灰色图
            faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags=cv2.cv.CV_HAAR_SCALE_IMAGE)                     #检测是否图像是否为人脸，并返回值赋值给faces
            for (x, y, w, h) in faces:
                if(faceflag==0):                                                                                                                            #判断faceflag是否为0                           
                    cv2.imwrite('image.jpg', frame,[int(cv2.IMWRITE_JPEG_QUALITY), 95])                                                                     #保存照片
                    faceUploadbit=Upload(frame,access_token,group_id_list)                                                                                  #上传图片
                cv2.putText(frame,"Face Detected!", ( 10, 10 ), cv2.FONT_HERSHEY_SIMPLEX, 0.3, ( 0, 0, 255 ), 1 )                                           #界面上方输出人脸被检测
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)                                                                                    #在图片人像上画正方形                
                if faceflag==10:                                                                                                                            #判断faceflag的值，若为10则faceflag为0，faceUploadbit为1
                    faceflag=0
                    faceUploadbit=1
            cv2.putText(frame,"No Face Detected!", ( 10, 10 ), cv2.FONT_HERSHEY_SIMPLEX, 0.3, ( 0, 0, 255 ), 1 )                                            #界面上方输出人脸未检测到
            cv2.imshow('Video', frame)                                                                                                                      #显示摄像头界面

            if cv2.waitKey(1) & 0xFF == ord('q'):                                                                                                           #判断是否按下q键，若按下则退出
                break
        video_capture.release()                                                                                                                             #释放摄像头资源
        cv2.destroyAllWindows()                                                                                                                             #关闭窗口
    else:
        print 'Access_token Get Fail！'                                                                                                                     #显示此输出，检查下网络是否通畅！
        Mains()                                                                                                                                             #重新执行Mains()，-----------------------------若显示该行数报错 则注销此句
Mains()
















    
#    while 1:
#        access_token=f.GetAccess_token(ApiKey,SecretKey)               #获取access_token
#        if(access_token):                                              #判断access_token是否获取成功
#            time.sleep(0.5)                                            #延时0.5秒                    
#            f.take_picture()                                           #拍下照片
#            img=f.open_picture()                                       #读取照片并编码为base64
#            output=f.FaceSearch (img,access_token,group_id_list)       #开始匹配并将反馈信息赋值给output
#            flag=f.ReadData(output,Similarity=70)                      #处理反馈信息并获取是否识别成功标志
#            if (flag):                                                 #判断标志是否为1
#                c.Open(pin)
#                time.sleep(3)
#                c.Stop(pin)
#            else
#                print '识别未成功！打开失败！'
#            time.sleep(3)                                              #延时3秒
#        else
#            print 'access_token获取失败！'


