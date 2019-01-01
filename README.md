Write By ITJoker Time:2018.10.08

[0x01]  If not, first: sudo apt-get install fswebcam & sudo apt-get install libv4l-dev

[0x02]  Python Version for 2.7.13  The Program Version is 1.0.0 Beta Version 

[0x03]  The required libraries are:
	urllib
	urllib2
	sys
	requests
	commands
	base64
	json
	os
	ssl
	time
	RPi.GPIO

[0x04]  If none of these libraries causes an error, the installation instruction format is�� sudo pip install xxx   #(xxxΪ����)

[0x05]  Configure it in main.py before use, otherwise the startup fails~

[0x06] Design idea:
    1. Through the imwrite() function in opencv, take pictures of the driveless USB camera and store them in image.jpg format.
    2. Then submit to baidu's face search API to realize face recognition through the post method in HTTP protocol.
    3. Then through the python rpi.gpio library to control the raspberry pie GPIO, to achieve the relay on and off state.

[0x07] How to use this Program
    1.Configuration of the main.py and fill in the baidu API(public key and secret key),also you can choose training set (lbpcascade_frontalface.xml or haarcascade_frontalface_default.xml)
	2.sudo python main.py
[0x08] This Program is a example,You can use this program to achieve the functions you want!!

[0x09] Bug can't Slove
	1.Currently unable to solve the problem of camera display screen is small

[0x10] If you like the project, give it to a star, or donate to the author alipay: 649258008@qq.com :)