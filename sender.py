import socket

ip = "128.4.60.146" #my current IP address
udp_port = 5005 #port associated with UDP

sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sckt.sendto("test", (ip, udp_port))