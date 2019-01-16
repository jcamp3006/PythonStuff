# -*- coding: utf-8 -*-

#import socket module
from socket import *
import time


serverPort = 9005
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)


serverPort2 = 9007
serverSocket2 = socket(AF_INET, SOCK_STREAM)
serverSocket2.bind(('',serverPort2))
serverSocket2.listen(1)

while True:
	#Establish the connection
	print "Server starting up"
	connectionSocket, addr =  serverSocket.accept() #create socket
	#Wait for stuff
	try:
		message = connectionSocket.recv(1024) 
		request= message.split()[0]
		
		if (request == "listFiles"):
			f = open("list.txt")
			outData = f.read()

			for i in range(0, len(outData)):
				connectionSocket.send(outData[i])

	 		connectionSocket.close()
	

		if (request == "sendFile"):
			fileName = message.split()[1]
			f = open(fileName)
			outputData = f.read()
			
			connectionSocket2, addr2 = serverSocket2.accept()
			counter = 0
			while counter <  len(outputData):
			
				message2 = connectionSocket2.recv(1024)
				request2 = message2.split()[0]	
				connectionSocket.send(outputData[counter])
		
				if (request2== "pause"):
					print "PAUSING"	
					flag = 1
			
					while flag:
						message3 = connectionSocket2.recv(1024)
						request3 = message3.split()[0]
						
						if (request3 == "play"):
							print "PLAYING"
							flag = 0
				
				if (request2 == "restart"):
					print "RESTARTING"
					counter = -1

				counter = counter + 1


			connectionSocket.send('^')
	 		connectionSocket.close()
		
	except IOError:
			connectionSocket.close()

serverSocket.close()
