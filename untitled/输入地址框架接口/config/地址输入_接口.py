#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

class 地址输入():
    def 地址_快查(self,*a):
        import requests

        url = "http://www.zhaoapi.cn/user/addAddr"

        payload = 'uid="{}"&addr="{}"&mobile="{}"&name="{}"&token="{}"'.format(a[0],a[1].encode('utf-8'),a[2],a[3],a[4])
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
            'Postman-Token': "747e9598-96ec-40f5-9c4a-9140364f6574"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)
        return response

a=地址输入()
a.地址_快查(22700,'北京市昌平区金域国际1-1-1',15837806865,15837806865,'B7674468CAC25325C13016653C09F3BD')

















#
# import requests
# class 地址输入():
#     def 地址_快查(self,*a):
#         url = "http://www.zhaoapi.cn/user/addAddr"
#
#         querystring = 'uid="{}",addr="{}",mobile="{}",name="{}",token="{}"'.format(a[0],a[1].encode('utf-8'),a[2],a[3],a[4])
#
#         payload = "undefined="
#         headers = {
#             'Content-Type':'application/x-www-form-urlencoded',
#             'cache-control': "no-cache",
#             'Postman-Token': "9099e0e5-b35a-408a-b6dd-dd1fe8c46190"
#         }
#
#         res = url.getresponse()
#         data = res.read()
#
#         print(data.decode("utf-8"))
# a=地址输入()
# a.地址_快查(22700,'北京市朝阳区',15837806865,15837806865,'B7674468CAC25325C13016653C09F3BD')
#
