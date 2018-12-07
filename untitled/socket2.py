import socket
# soo=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# soo.connect(('192.168.0.57',3333))
# aaa='2142142'
# soo.send(aaa.encode('utf-8'))
# msg=soo.recv(1024)
# print(msg.decode('utf-8'))

s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.connect(('192.168.0.57',3333))
aaa='内容明确'
s1.send(aaa.encode('utf-8'))
m=s1.recv(1024)
print(m.decode('utf-8'))