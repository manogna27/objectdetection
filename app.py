import cv2
import numpy as np
import time
import playsound
from gtts import gTTS
import os
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename
from tkinter import scrolledtext as st 



#--defining functions

def webcam():
    #exec(open(object_detect.py).read())
	os.system('python webcamera.py')
	
def openvideo():
    #exec(open(object_detect.py).read())
	os.system('python video.py')
	
def openimage():
    #exec(open(object_detect.py).read())
	os.system('python image.py')

#--GUI
root=tk.Tk();
root.geometry("900x500")
root.title('Object Detection')
root['bg'] = 'gray90'



label = tk.Label(root, text = "Object Detection With Speech Synthesis", font =('Verdana', 12))
label.pack(padx = 30, pady = 30)


click_btn1= PhotoImage(file='web.png')
img_label= Label(image=click_btn1)

click_btn2= PhotoImage(file='img.png')
img_label= Label(image=click_btn2)

click_btn3= PhotoImage(file='vid.png')
img_label= Label(image=click_btn3)

button1= Button(root, image=click_btn1,command= lambda:webcam())
button1.place(x=100, y=100)

button2= Button(root, image=click_btn2,command= lambda:openimage())
button2.place(x=350, y=100)

button3= Button(root, image=click_btn3,command= lambda:openvideo())
button3.place(x=600, y=100)


root.mainloop()