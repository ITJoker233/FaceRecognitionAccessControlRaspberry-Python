# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time

#Write By ITJoker Time：2018.10.08
#若无法使用，则先 sudo apt-get install fswebcam

#test pin=7
def Init(pin): #初始化端口

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(pin,GPIO.OUT)

    
def Open(pin): #打开端口

    GPIO.output(pin, True)

    
def Stop(pin): #关闭端口

    GPIO.output(pin,False)
    GPIO.cleanup()
