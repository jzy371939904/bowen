import  socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a=('192.168.0.57',3333)
# s.bind(a)
# s.listen(5)
# while True:
#     a,b=s.accept()
#     msg=a.recv(1024)
#     print(msg.decode('utf-8'))
#     reg='内容'
#     a.send(reg.encode('utf-8'))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
a=('192.168.0.57',3333)
s.bind(a)
s.listen(6)
while True:
    a,b=s.accept()
    msg=a.recv(1024)
    print(msg.decode('utf-8'))
    r='xiaozhenzhendafksajdflsaknglasjkg'
    a.send(r.encoed('utf-8'))

