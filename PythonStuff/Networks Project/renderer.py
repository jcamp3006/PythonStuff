from socket import *
import socket
import sys

serverPort = 9006
serverSocket = socket.socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
	#Establish connection
	
	print 'Rederer starting up'
	connectionSocket, addr = serverSocket.accept() #create socket
	
	try:
		message = connectionSocket.recv(1024)
		request = message.split()[0]

		if (request == "fileName"):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect(('10.0.0.3', 9005))
			filename= message.split()[1]
			s.sendall("sendFile" + " " + filename)
			
			flag = 1

			while flag:
				data = s.recv(1)
				
				if (data != ''):
					print str(data)
				
				if (data == '^'):
					flag = 0

			s.close()

		connectionSocket.close()



	except IOError:
		connectionSocket.close()


serverSocket.close()
