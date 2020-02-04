from tkinter import *
import time
import socket

#<--------------------------------defining the main window class------------------------->

class main_window(Tk): #inheriting from the Tk class
	def __init__(self): #defining the constructor of the main_window class
		super().__init__() #calling the constructor of the Tk class
		self.title("my app")
		self.geometry("600x400")
		self.config(bg = 'blue')
		top_frame = Frame(self,bg = 'blue')
		top_frame.pack(pady = 20,side = TOP)
		intro_label = Label(top_frame,text = "WELCOME TO RASPBERRY PI CLIENT CONTROLLER",font = 'helvatica 16 bold',bg = 'blue',fg = 'yellow')
		intro_label.pack(padx = 10,pady = 10)
		bottom_frame = Frame(self,bg = 'brown')
		bottom_frame.pack(pady = 20,side = TOP)
		option_button = Button(bottom_frame,text = 'OPTION',padx = 10,pady = 10,font = 'helvatica 12 bold',bg = 'black',fg = 'green')
		manual_control_button = Button(bottom_frame,text = 'MANUAL MODE',padx = 10,pady = 10,font = 'helvatica 12 bold',bg = 'black',fg = 'green')
		ai_control_button = Button(bottom_frame,text = 'AI MODE',padx = 10,pady = 10,font = 'helvatica 12 bold',bg = 'black',fg = 'green')
		option_button.pack(padx = 20,pady = 20)
		manual_control_button.pack(padx = 40,pady = 20)
		ai_control_button.pack(padx = 40,pady = 20)


root = main_window()



root.mainloop()


