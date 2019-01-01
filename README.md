Write By ITJoker Time:2018.10.08<br>
Update Time:2019.01.01<br>
<strong>[0x01]:</strong>  If not, first: sudo apt-get install fswebcam & sudo apt-get install libv4l-dev<br>

<strong>[0x02]:</strong>   Python Version for 2.7.13  The Program Version is 1.0.0 Beta Version <br>

<strong>[0x03]:</strong>   The required libraries are: <br>
	urllib <br>
	urllib2 <br>
	sys <br>
	requests <br>
	commands <br>
	base64 <br>
	json <br>
	os <br>
	ssl <br>
	time <br>
	RPi.GPIO <br>
<br>
<strong>[0x04]:</strong>   If none of these libraries causes an error, the installation instruction format is： sudo pip install xxx   #(xxx is librarie name)<br>

<strong>[0x05]:</strong>   Configure it in main.py before use, otherwise the startup fails~<br>

<strong>[0x06]:</strong>  Design idea:<br>
    1. Through the imwrite() function in opencv, take pictures of the driveless USB camera and store them in image.jpg format. <br>
    2. Then submit to baidu's face search API to realize face recognition through the post method in HTTP protocol. <br>
    3. Then through the python rpi.gpio library to control the raspberry pie GPIO, to achieve the relay on and off state. <br>
<br>
<strong>[0x07]:</strong>  How to use this Program<br>
    1.Configuration of the main.py and fill in the baidu API(public key and secret key),also you can choose training set (lbpcascade_frontalface.xml or haarcascade_frontalface_default.xml)<br>
	2.sudo python main.py <br>
<br>
<strong>[0x08]:</strong>  This Program is a example,You can use this program to achieve the functions you want!!<br>

<strong>[0x09]:</strong>  Bug can't Slove<br>
	1.Currently unable to solve the problem of camera display screen is small <br>
<br>
<strong>[0x10]:</strong>  If you like the project, give it to a star, or donate to the author alipay: 649258008@qq.com :)
