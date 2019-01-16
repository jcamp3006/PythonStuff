from socket import *
import socket
import sys
import thread
import time

def main():

	flag = 1
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('10.0.0.3', 9005))
	s.sendall("listFiles")

	data = s.recv(1024)
		
	if (data != ''):
		print "Response from server: " + str(data)

		s.close()

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(('10.0.0.2', 9006))


		fileName = raw_input("Which file would you like stream? ")
		s.sendall("fileName" + " " + fileName)
		flag = 0
		s.close()
	stage2()


def stage2():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('10.0.0.3', 9007))

	stuff(s)
	main()	


def stuff(s):

	flagStuff = 1 
	createFlag = 1
	a_list = 1
	counter = 0
	while flagStuff:
		if (createFlag == 1):
			a_list = []
			thread.start_new_thread(input_thread,(a_list, createFlag))
			createFlag = 0
		
		while not a_list:
			time.sleep(1)
			s.sendall(str(counter))
			counter = counter + 1
		
		command = raw_input("Enter a command: ")

		if (command == "kill"):
			flagStuff = 0
	
		s.sendall(command)
		createFlag = 1



def input_thread(a_list, createFlag):
	raw_input()
	a_list.append(True)



main()
