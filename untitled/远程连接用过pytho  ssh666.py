#！/usr/bin/env python
# -*- coding:utf-8 -*-
import paramiko
ssh666=paramiko.SSHClient() #创建一个ssh客户端
ssh666.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#把你要连接的主机添加到knpow_hosts文件中
# ssh666.connect(hostname='192.168.0.164',
#                port=22,
#                username='root',
#                password='111111')
# shuin,stuout,stuerr=ssh666.exec_command("ls -al")#你要执行的命令写在括号理
# print(stuout.read().decode()) #打印
# ssh666.close()  #断开命令

# while True:
#     a=input(">>>>>>")
#     if a=='exit':
#         break
#     else:
#         shuin,stuout,stuerr = ssh666.exec_command(a)
#         print(stuout.read().decode())
# ssh666.close()



ssh666=paramiko.Transport(('ip',22))
ssh666.connect(username='root',password='root密码')

sftp=paramiko.SFTPClient.from_transport(ssh666)
#get是从linux下载文件到本地
sftp.get('linux目录/文件名','本地目录/文件名')

#put是从本地向linux上传文件
sftp.put('本地目录/文件名','linux目录/文件名')

sftp.close() #断开连接

