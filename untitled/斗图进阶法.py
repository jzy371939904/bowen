import requests
import re
import os
# class doutu():
#     def wz(self,page):
#         url='http://www.doutula.com/article/list/?page={}'.format(page)
#         head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#         response=requests.get(url=url,headers=head)
#         html=response.content.decode('utf-8')
#         print(html)
#         return html
#     def guolv(self,aaa):
#         shuju=[]
#         patt=re.compile(r'https://www.doutula.com/article/detail/[0-9]{7}')
#         items=patt.findall(aaa)
#         for i in items:

def wangzhi():
    url='https://www.doutula.com/article/list/?page=5'
    head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    res=requests.get(url=url,headers=head)
    html=res.content.decode('UTF-8')
    patt=re.compile(r'https://www.doutula.com/article/detail/[0-9]{7}',re.S)
    items=patt.findall(html)
    return items
a=wangzhi()
# print(a)
def baocun(b):
    for q,i in enumerate(b):
        i=i.replace( '">' ,'')
        os.mkdir(r'C:\Users\jzy\Desktop\新建文件夹{}'.format(q))
        # print(i)
        url=i
        head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        res = requests.get(url=url, headers=head)
        html1 = res.content.decode('UTF-8')
        patt1 = re.compile(r'onerror="this.src=(.*?)"', re.S)
        items1=patt1.findall(html1)
        # print(items1)
        for k,j in enumerate(items1):
            j=j.replace(',','')
            j=j.replace("'",'')
            tupian = requests.get(j)
            res1 = tupian.content
            with open(r'C:\Users\jzy\Desktop\新建文件夹{}\{}.jpg'.format(q,k), 'wb') as f:
                f.write(res1)
baocun(a)


