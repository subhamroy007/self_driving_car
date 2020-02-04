from tkinter import *
import socket
import time

#<---------------------------creating option window class--------------------------->


class option_window(Tk):
	def __init__(self):
		super().__init__()
		self.geometry('580x400')
		self.title('option window')
		self.config(bg = 'blue')
		directory_label = Label(self,text = 'choose directory to store data',font = 'helvatica 18 italic',padx = 10,pady = 10,fg = 'yellow',bg = 'blue')
		directory_button = Button(self,text = 'BROWSE',font = 'helvatica 14 italic',padx = 5,pady = 5,fg = 'yellow',bg = 'brown')
		directory_label.grid(row = 0,column = 0,padx = 10,pady = 40)
		directory_button.grid(row = 0,column = 1,padx = 10,pady = 40)
		connection_label = Label(self,text = 'click to connect with a server',font = 'helvatica 18 italic',padx = 10,pady = 10,fg = 'yellow',bg = 'blue')
		connection_button = Button(self,text = 'CONNCET',font = 'helvatica 14 italic',padx = 5,pady = 5,fg = 'yellow',bg = 'brown')
		connection_label.grid(row = 1,column = 0,padx = 10,pady = 10)
		connection_button.grid(row = 1,column = 1,padx = 10,pady = 10)
		data_label = Label(self,text = 'collect data while driving?',font = 'helvatica 18 italic',padx = 10,pady = 10,fg = 'yellow',bg = 'blue')
		data_checkbutton = Checkbutton(self,font = 'helvatica 14 italic',fg = 'black',bg = 'blue')
		data_label.grid(row = 2,column = 0,pady = 40)
		data_checkbutton.grid(row = 2,column = 1,pady = 40)
		ok_button = Button(self,text = 'CONFIRM',font = 'helvatica 14 bold',padx = 5,pady = 5,fg = 'yellow',bg = 'brown')
		cancel_button = Button(self,text = 'CANCEL',font = 'helvatica 14 bold',padx = 5,pady = 5,fg = 'yellow',bg = 'brown')
		ok_button.grid(row = 3,column = 0,padx = 20,pady = 10)
		cancel_button.grid(row = 3,column = 1,padx = 20,pady = 10)






option_root = option_window()

option_root.mainloop()