import socket
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect(('192.168.0.75',5555))
aaa='66666666'
soc.send(aaa.encode('utf-8'))
msg=soc.recv(1024)
print(msg.decode('utf-8'))