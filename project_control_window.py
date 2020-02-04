from tkinter import *
import socket
import time
from PIL import Image,ImageTk
#<---------------------------creating control window class--------------------------->

class control_window(Tk):
	def __init__(self):
		super().__init__()
		self.geometry('600x460')
		self.title('control window')
		self.config(bg = 'blue')
		frame1 = Frame(self,bg = 'blue')
		frame2 = Frame(self,bg = 'blue')
		frame3 = Frame(self,bg = 'blue')
		frame4 = Frame(self,bg = 'blue')
		frame1.pack(pady = 20)
		frame2.pack(pady = 20)
		frame3.pack(pady = 20)
		frame4.pack()
		forward_label = Label(frame1,text = '/\\\n|\nW',font = 'helvatica 24 bold',bg = 'brown',fg = 'yellow',padx = 10)
		left_label = Label(frame2,text = '<-- A',font = 'helvatica 24 bold',bg = 'brown',fg = 'yellow',padx = 40)
		right_label = Label(frame2,text = 'D -->',font = 'helvatica 24 bold',bg = 'brown',fg = 'yellow',padx = 40)
		backward_label = Label(frame3,text = 'S\n|\n\\/',font = 'helvatica 24 bold',bg = 'brown',fg = 'yellow',padx = 10)
		forward_label.pack()
		left_label.pack(side = LEFT,padx = 30)
		right_label.pack(side = LEFT,padx = 30)
		backward_label.pack()
		exit_button = Button(frame4,text = 'EXIT CONNECTION AND QUIT',font = 'helvatica 18 italic',fg = 'green',bg = 'black')
		exit_button.pack()

control_root = control_window()

control_root.mainloop()