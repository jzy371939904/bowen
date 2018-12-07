import  socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
a=('192.168.0.75',5555)
s.bind(a)
s.listen(5)
while True:
    a,b=s.accept()
    msg=a.recv(1024)
    print(msg.decode('utf-8'))
    reg='小珍珍真丑'
    a.send(reg.encod('utf-8'))