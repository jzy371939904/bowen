import requests
import re
import urllib3
urllib3.disable_warnings()
url='http://www.dagumanhua.com/manhua/12687/'
head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
response=requests.get(url=url,headers=head,verify=False)
html=response.content.decode('utf-8')
# print(html)
patt=re.compile(r'<li><a href=(.*?)</p><i></i></a></li>',re.S)
items=patt.findall(html)
for i in items:
    i=i.replace('"/','')
    i='https://www.dagu'+i
    j=i.split('"')[0]
    for h in range(1,13):
        if h==1:
            url=j
        else:
            j=j.replace('.html','_{}.html'.format(h))
            url=j
        patt1=re.compile(r'<img src=(.*?)</a></p></div>',re.S)
        items1=patt1.findall(j)
        print(items1)
        # for n,m in enumerate(items1):
        #     tupian=requests.get(m)
        #     res1=tupian.content
        #     with open(r'C:\Users\jzy\Desktop\新建文件夹\{}'.format(n),'wb')as f:
        #         f.write(res1)





















# def tupian(page):
#     url='https://www.dagumanhua.com/manhua/12687/357060.html'or 'https://www.dagumanhua.com/manhua/12687/357060_{}.html'.format(page)
#     head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
