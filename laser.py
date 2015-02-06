#k!/usr/bin/python
# -*- coding: utf-8 -*-

# """
# ZetCode Tkinter tutorial

# This program creates a quit
# button. When we press the button,
# the application terminates. 

# author: Jan Bodnar
# last modified: December 2010
# website: www.zetcode.com
# """

from Tkinter import Tk, BOTH

from ttk import Frame, Button, Style, Scale, Label
import serial
global ser
ser = serial.Serial('/dev/ttyACM0', 115200) 
# global Xpos
# global Ypos
# Xpos = 0
# Ypos = 0
# a= 100
# global da
# da = 20 * 4
global motor0
global motor1


class Stepper():
	def __init__(self, motor_number):
		self.angle = 50
		self.pos = 0
		self.mot_pos = " "
		self.mot_num = str(motor_number)
		self.max_accel = "100"
	def send(self):
		global ser
		self.mot_pos = str(self.pos)
		ser.write("{" + self.mot_num + ";" + self.mot_pos + ";" + self.max_accel + "}")
	def clockwise(self):
		self.pos = self.pos - self.angle
		self.send()
	def counterclockwise(self):
		self.pos = self.pos + self.angle
		self.send()
	def setstep(self, angle): 
		
#		if (angle == 0 ):
#			angle = 5
#		if (angle > 50): #arbitraty limits
#			angle = 50
		self.angle = angle * 4# Multiples of four because we're doing...micro steps?

motor1 = Stepper(0)
motor0 = Stepper(1)
def getpos():
	print(ser.read(10))
	

def up():
	# global Ypos
	# global da
	# Ypos = Ypos - da
	# ser.write("{ 1;" + str(Ypos) + ";100}")
	global motor0
	motor0.clockwise()
def down():
	# global Ypos
	# global da
	# Ypos = Ypos + da
	# ser.write("{ 1;" + str(Ypos) + ";100}")
	global motor0
	motor0.counterclockwise()
def left():
	# global Xpos
	# global da
	# Xpos = Xpos - da
	# ser.write("{ 0;" + str(Xpos) + ";100}")
	global motor1
	motor1.clockwise()
def right():
	# global Xpos
	# global da
	# Xpos = Xpos + da
	# ser.write("{ 0;" + str(Xpos) + ";100}")
	global motor1
	motor1.counterclockwise()
def set_step():
	global motor1
	global motor0
	global AngleSlider
	angle = AngleSlider.get()
	motor0.setstep(angle)
	motor1.setstep(angle)
def ledtoggle():
	ser.write("led")
def blacklighttoggle():
	ser.write("blacklight")
def idle():
	ser.write("reset")
	motor0.pos = 0
	motor1.pos = 0




		
class Gui1(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent)   
		self.parent = parent
		self.initUI()
		
  	def initUI(self):
		global AngleSlider
	
		motor0 = Stepper(0)
		motor1 = Stepper(1)
		
		self.parent.title("Turrets, aaagh")
		self.style = Style()
		self.style.theme_use("default")
		self.pack(fill=BOTH, expand=1)
		quitButton = Button(self, text="Quit", command=self.escape)
		upButton = Button(self, text="Up!", command = up)
		downButton = Button(self, text="Down!", command = down)
		leftButton = Button(self, text="left!", command = left)
		rightButton = Button(self, text="right!", command = right)
		idleButton = Button(self, text="Idle", command = idle)
		ledButton = Button(self, text="toggle red dot", command = ledtoggle)
		blacklightButton = Button(self, text="toggle blacklight", command = blacklighttoggle)
		AngleSlider = Scale(self, from_=1, to=90)
		setButton = Button(self, text="Set Step", command = set_step)
		setButton.pack(side="bottom")
		AngleSlider.pack(side = "bottom")
		ledButton.place(x = 100, y = 200)
		blacklightButton.place(x = 250,y = 200)
		quitButton.place(x=0, y=100)
		upButton.place(x=500/2, y=0)
		downButton.place(x = 500/2, y = 50)
		leftButton.place(x = 500/3, y = 25)
		rightButton.place(x = 2*500/3, y = 25)
		idleButton.place(x = 0, y = 200)
		label = Label(self, text="Step Angle: " + str(AngleSlider.get()))
		label.pack(side="bottom")
		
	def escape(self):
		idle()
		self.quit()
def main():
	
	

	root = Tk()
	root.geometry("500x300+300+300")
	app = Gui1(root)
	root.mainloop()  


if __name__ == '__main__':
    main()  
