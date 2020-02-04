from tkinter import *
import time
import socket
import tkinter.messagebox as msg
import io
import threading
import struct
import cv2
import numpy as np
import pygame
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy
import os



json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
#load weights into new model
loaded_model.load_weights("model.h5")

#loaded_model.compile(optimizer = 'adam',loss = 'categorical_crossentropy',metrics = ['accuracy'])
connection = None
terminator = False
port_no = 3000
x = 'n'
address_no = '192.168.43.245'
client_sock = socket.socket()#initializing the socket for the server port
#client_sock.bind(('192.168.43.235',3000))





def key_down(event):
	global client_sock
	x = event.char
	if x == 'w':
		client_sock.send(x.encode())
		print("forward")
	elif x == 's':
		client_sock.send(x.encode())
		print("backward")
	elif x == 'a':
		client_sock.send(x.encode())
		print("leftward")
	elif x == 'd':
		client_sock.send(x.encode())
		print('rightward')
	else:
		pass

def key_up(event):
	global client_sock
	x = 'n'
	client_sock.send(x.encode())
	print('neutral')



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
		option_button = Button(bottom_frame,text = 'OPTION',padx = 10,pady = 10,font = 'helvatica 12 bold',bg = 'black',fg = 'green',command = self.option_click)
		manual_control_button = Button(bottom_frame,text = 'MANUAL MODE',padx = 10,pady = 10,font = 'helvatica 12 bold',bg = 'black',fg = 'green',command = self.manual_click)
		ai_control_button = Button(bottom_frame,text = 'AI MODE',padx = 10,pady = 10,font = 'helvatica 12 bold',bg = 'black',fg = 'green',command = self.ai_mode)
		option_button.pack(padx = 20,pady = 20)
		manual_control_button.pack(padx = 40,pady = 20)
		ai_control_button.pack(padx = 40,pady = 20)

	def option_click(self):
		option_window_root = option_window()

		option_window_root.mainloop()

	def manual_click(self):
		control_thread = threading.Thread(target = control_window_func,name = "control thread",args = ())
		stream_thread = threading.Thread(target = streamer,name = "stream thread",args = ())
		control_thread.start()
		stream_thread.start()
		#control_thread.join()
		#stream_thread.join()
	def ai_mode(self):
		global loaded_model
		global connection
		global client_sock
		#global terminator
		global x
		#counter = 0
		#path = 'C:/Users/subha/Desktop/python_codes/project1'
		cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
		try:
			while True:
				image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
				if not image_len:
					break
				image_stream = io.BytesIO()
				image_stream.write(connection.read(image_len))
				image_stream.seek(0)
				file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
				img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
				cv2.imshow("Image", img)
				cv2.waitKey(1)
				img = cv2.resize(img,(32,32))
				img = np.reshape(img,[1,32,32,3])

				im_pred = loaded_model.predict(img)
				im_pred = im_pred[0]
				if im_pred[0] == 1:
					x = 'a'
					client_sock.send(x.encode())
				elif im_pred[1] == 1:
					x = 'd'
					client_sock.send(x.encode())
				elif im_pred[2] == 1:
					x = 's'
					client_sock.send(x.encode())
				else:
					x = 'w'
					client_sock.send(x.encode())
					
					

		except:
			pass
		


def streamer():
	global connection
	global terminator
	global x
	counter = 5000
	path = 'C:/Users/subha/Desktop/python_codes/project1'
	cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
	try:
		while terminator == False:
			image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
			if not image_len:
				break
			image_stream = io.BytesIO()
			image_stream.write(connection.read(image_len))
			image_stream.seek(0)
			file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
			img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
			cv2.imshow("Image", img)
			cv2.waitKey(1)
			if x != 'n':
				cv2.imwrite(path+'/'+x+'/'+str(counter)+'.png',img)
				counter += 1

	except:
		pass
	#finally:
		#connection.close()
		#client_sock.close()


def control_window_func():
	global client_sock
	global connection
	global terminator
	global x
	x = 'n'
		#manual_window_root = control_window()

		#manual_window_root.mainloop()
	pygame.init()

	white = (255,255,255)
	black = (0,0,0)
	red = (255,0,0)
	green = (0,255,0)
	blue = (0,0,255)
	forward_img = pygame.image.load('up.png')
	backward_img = pygame.image.load('down.png')
	leftward_img = pygame.image.load('left.png')
	rightward_img = pygame.image.load('right.png')


	gameDisplay = pygame.display.set_mode((600,400))
	gameDisplay.fill(blue)
	pygame.display.set_caption('test game display')


	gameExit = False

	while not gameExit:

		gameDisplay.blit(forward_img,(270,50))
		gameDisplay.blit(backward_img,(270,230))
		gameDisplay.blit(leftward_img,(150,170))
		gameDisplay.blit(rightward_img,(330,170))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				x = 'q'
				terminator = True
				client_sock.send(x.encode())
				connection.close()
				client_sock.close()
				msg.showinfo("client server msg","disconnected with server")
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					x = 'w'
					client_sock.send(x.encode())
					print("car is moving forward")
				if event.key == pygame.K_s:
					x = 's'
					client_sock.send(x.encode())
					print("car is moving backward")
				if event.key == pygame.K_a:
					x = 'a'
					client_sock.send(x.encode())
					print("car is moving left")
				if event.key == pygame.K_d:
					x = 'd'
					client_sock.send(x.encode())
					print("car is moving right")

			if event.type == pygame.KEYUP:
				x = 'n'
				client_sock.send(x.encode())
				print("car is neutral")


	pygame.quit()






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
		connection_button = Button(self,text = 'CONNCET',font = 'helvatica 14 italic',padx = 5,pady = 5,fg = 'yellow',bg = 'brown',command = self.server_connect)
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

	def server_connect(self):
		global port_no
		global address_no
		global client_sock
		global connection

		try:
			client_sock.connect((address_no,port_no))
			connection = client_sock.makefile('rb')
			msg.showinfo("client server msg","successfully connected with server")
		except:
			val = msg.askretrycancel("client server msg","error occured during connection")
			if val == True:
				self.server_connect()
			else:
				pass




#<---------------------------creating control window class--------------------------->

class control_window(Tk):
	def __init__(self):
		super().__init__()
		self.geometry('600x460')
		self.title('control window')
		self.config(bg = 'blue')
		self.bind('<Key>',key_down)
		self.bind('<KeyRelease>',key_up)
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
		exit_button = Button(frame4,text = 'EXIT CONNECTION AND QUIT',font = 'helvatica 18 italic',fg = 'green',bg = 'black',command = self.destroy_all)
		exit_button.pack()



	def destroy_all(self):
		global client_sock
		x = 'q'
		client_sock.send(x.encode())
		client_sock.close()
		msg.showinfo("client server msg","disconnected with server")
		self.destroy()




root = main_window()


root.mainloop()
