# FaceRecognitionAccessControlRaspberry

**Using `python`**

---

> Write By ITJoker Time:2018.10.08

>Update Time:2019.01.01

>Program Version:beta-1.0

## Design Idea

- Through the `imwrite()` function in opencv, take pictures of the driveless USB camera and store them in `image.jpg` format.
- Then submit to baidu's face search API to realize face recognition through the post method in HTTP protocol.
- Then through the python `rpi.gpio` library to control the raspberry pie GPIO, to achieve the relay on and off state.

## Depends
- Python Version `2.7.13` or higher(**Does not support `Python3`**)

- You should execute commands below:

```shell
sudo apt-get install fswebcam libv41-dev git
pip install requests
pip install commands
```

- Then clone this repositories

```shell
git clone https://github.com/ITJoker233/FaceRecognitionAccessControlRaspberry-Python
```

## Program Guide
1. Configuration of the main.py and fill in the baidu API*(public key and secret key)*.

	Also you can choose training set (`lbpcascade_frontalface.xml` or `haarcascade_frontalface_default.xml`)

2. Execute the `main.py` using root access

---

**This Program is a example,You can use this program to achieve the functions you want!!**

---

## Recently Bugs
- Currently unable to solve the problem of camera display screen is small

---

***If you like the project, give it to a star, or donate to the author.https://blog.itjoker.cn/donate :)***
