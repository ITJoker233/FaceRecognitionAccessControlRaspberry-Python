# -*- coding: UTF-8 -*-
import urllib, urllib2, sys,requests #导入urllib, urllib2, sys,requests，json，os base64库
import commands
import base64,json,os,cv2
import time
import ssl

#Write By ITJoker Time：2018.10.10
#若无法使用，则先 sudo apt-get install fswebcam


def GetAccess_token(ApiKey,SecretKey): #获取access_token，通过request请求

    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + str(ApiKey) + '&client_secret='+ str(SecretKey) #request的地址及提交的数据
    request = urllib2.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib2.urlopen(request)
    content = response.read()
    if (content):
        access_token=json.loads(content)['access_token']
    return access_token                                                                                                                         #返回access_token


def take_picture():     #拍摄当前图片    此函数会与主函数冲突导致奔溃 切勿使用！ 

    (status, output) = commands.getstatusoutput('sudo fswebcam --no-banner -r 640x480 image.jpg')                                  #执行拍照命令
    print status, output                                                                                                           #输出执行信息


    
def open_picture():     #读取照片转换成base64格式

    fileimg = open('image.jpg', 'rb')                                                                                              #打开image.jpg文件
    img = base64.b64encode(fileimg.read())                                                                                         #读取文件并为值编码为base64的格式
    return img                                                                                                                     #返回 img的值


def FaceSearch (img,access_token,group_id_list="test_1"): #得到图片的base64加密的字符串,通过request.post方法发送

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"                                                               #提交的地址
    params = {"image":img,"image_type":"BASE64","group_id_list":group_id_list,"quality_control":"LOW","liveness_control":"NORMAL"} #定义Post发送的Json格式
    request_url = request_url + "?access_token=" + access_token                                                                    #加上请求的access_token
    response = requests.post(request_url, data=params)                                                                             #提交数据，返回的值到response
    output = response.json()                                                                                                       #json序列化给output
    return output                                                                                                                  #返回output值


def ReadData (output,Similarity=70): #读取Josn数组，并判断匹配结果,Similarity（相似度）的值默认为70

    if output['error_code'] == 0:                                                                                                  #判断是否识别成功
        user_list= output['result']['user_list']                                                                                   #找到字典里的result－以及内层字典里的user_list
        score = user_list[0]['score']                                                                                              #利用列表的检索方式找到列表里的人脸检测分数－score
        if score >= Similarity:                                                                                                    #判断相似度是否达到70以上
            print '识别成功!'
            return 1
        else :
            print '相似度过低!识别失败!'
            return 0
    else:
        if output['error_code']==222202:
            print '识别失败!未检测到人脸!'
            return 0
        elif output['error_code']==222207:
            print '识别失败!未找到匹配的用户!'
            return 0
        elif output['error_code']==223114:
            print '识别失败!请拍摄时不要晃动设备！'
            return 0
        elif output['error_code']==223115:
            print '识别失败!请光线适宜的地方拍摄!'
            return 0
        elif output['error_code']==223116:
            print '识别失败!请勿遮挡面部!'
            return 0
