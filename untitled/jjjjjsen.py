import json

date={'name':666,'小珍珍':777}
date1=json.dumps(date) #讲字典更改为json字符串 （数据）

date2=json.loads(date1) # 讲json数据更改为字典

print(type(date1))
print(type(date2))
print(date1)













