
# 99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(j,i,i*j),end = "\t")
    print()


#质数之和
s=0
for i in range(2,101):
    for j in range(2,i+1):
        if i%j==0:
            break
    if  i==j:
        s+=i
print(s)


#1+2-3+4-5+6-7.。。。





# 1，把字符串变成整数
a="545464164654165465165"
b=a[::-1]
s=0
for i,j in enumerate(b):
    for k in range(10):
        if str(k)==j:
            s+=k*10**i
print(s)

#回文字符串
a='123321'
b=len(a)//2
# c=0
for c in range(b):
    if a[c]!=a[-c-1]:
        print('yes')
else:
     print('no')


# #不用int将字符串变成整数
# a=input('>>>>')
# b=a.split(',')
# for i in range(len(b)):
#     print(type(b))



# #去除重排序
# a=[234,123,324,234,234,2215,151,5,2536,2352345,462534,1,112435,124,235,23,41,41,5]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# for j in range(len(b)):
#     for k in range(len(b)-1):
#         if













