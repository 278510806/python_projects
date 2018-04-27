import http.client_

conn=http.client.HTTPSConnection('www.baidu.com')
#发送请求
conn.request('GET','/')
#获取响应
r=conn.getresponse()

print(r.status,r.reason)

for line in r.readlines():
    print(line)