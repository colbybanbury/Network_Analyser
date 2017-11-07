import socket

ip = "128.4.60.146" #my current ip
udp_port = 5005	#port associated with UDP

sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sckt.bind((ip, udp_port))

while 1:
	message, address = sckt.recvfrom(1024) #1024 bytes is the buffer size
	print "message is: ", message