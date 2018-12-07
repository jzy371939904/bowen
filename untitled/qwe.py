#/usr/bin/env python
# -*- coding:utf-8 -*-
class jihe(object):
    def __init__(self,x,y):  #初始化属性
        self.n1=x
        self.n2=y
    def zhishu(self):
        s=0
        for i in range(self.n1,self.n2):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                    s+=i
        return s
    def huiwen(self):
        a=self.n1
        b=(a[::-1])
        for i in range(len(b)):
            if a[i] != a[-i-1]:
                print('no')
                break
        else:
            print('yes')

# a=jihe(x,y)
# print(a.zhishu(20,50))
jihe=jihe("66",'1234')
#print(jihe.zhishu())
jihe.huiwen()



