#！/usr/bin/env python
# -*- ccoding:UTF-8 -*-

import  requests
import  re
import urllib3
import pymysql
import xlrd
import xlwt



url='https://www.zhipin.com/job_detail/?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&scity=101210100&industry=&position='
head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
response=requests.get(url=url,headers=head,verify=False)
html=response.content.decode('utf-8')
# print(html)
patt=re.compile(r'<div class="job-title">(.*?)</div>',re.S)
patt1=re.compile(r'custompage" target="_blank">(.*?)</a></h3>',re.S)
patt2=re.compile('<span class="red">(.*?)</span>',re.S)
patt3=re.compile('<div class="info-detail"></div>(.*?)</p>',re.S)

items=patt.findall(html)
items1=patt1.findall(html)
items2=patt2.findall(html)
items3=patt3.findall(html)
# print(len(items))
# for i in items,items1,items2,items3:
#     print(i)
# f=xlwt.Workbook()
# sheet=f.add_sheet('66666.xls')
#
# for i,j in enumerate(items):
#     # i=i.strip()
#     # print(i)
#     sheet.write(i,0,j)
#     f.save('666.xls')
#
#
# for i,j in enumerate(items1):
#     # i=i.strip()
#     # print(i)
#     sheet.write(i,1,j)
#     f.save('666.xls')
#
#
# for i,j in enumerate(items2):
#     # i=i.strip()
#     # print(i)
#     sheet.write(i,2,j)
#     f.save('666.xls')
#
#
# for j,i in enumerate(items3):
#     i=i.replace('</a>',' ')
#     i = i.replace('</h3>', ' ')
#     i = i.replace('<p>', ' ')
#     i = i.replace('"/', ' ')
#     i = i.replace('<em class="vline"></em>', ' ')
#     i = i.strip()
#     sheet.write(j,3,i)
#     f.save('666.xls')
#     print(i)

f=xlrd.open_workbook('666.xls')
sheet=f.sheets()[0]






abc=pymysql.connect(host='192.168.0.84',
                    port=3306,
                    user='root',
                    password='654321',
                    charset='utf8')
aaa=abc.cursor()
#aaa.execute('create database jzy999;')
aaa.execute('use jzy999;')
aaa.execute('create table biaoo(职位名称 char(255),公司名称 char(255),月收入 char(255),公司地址 char(255));')
b=sheet.nrows
for i in range(b):
    c=sheet.row_values(i)
    aaa.execute('insert into biaoo values("{}","{}","{}","{}");'.format(c[0],c[1],c[2],c[3]))
    abc.commit()
aaa.execute('select * from biaoo;')
for i in aaa.fetchall():
    print(i)













