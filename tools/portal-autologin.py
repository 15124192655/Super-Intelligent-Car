#forgive my poor English
from urllib import request,parse
import sys
import re


def gethttp(url,char='utf-8'):
    with request.urlopen(url) as f:
        data = f.read()
        return f.status,data.decode(char)

def postdata(url,data,char='utf-8'):
    req=request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
    with request.urlopen(req, data=data.encode(char)) as f:
        return f.status,f.read().decode(char)

def login_gate1(user,passwd):
    url='http://10.3.8.216'

    login_data = parse.urlencode([
        ('user', user),
        ('pass', passwd),
    ])
    code,resp=postdata(url,login_data)

    if code!=200:
        return False,'network error'
    if re.search('successfully',resp)==None:
        return False,'user or password is wrong'
    else:
        return True,'ok'
def login_gate2(user,passwd):
    url='http://10.3.8.211'

    login_data=parse.urlencode([
        ("DDDDD",user),
        ('upass',passwd),
        ('0MKKey',''),
    ])
    code,resp=postdata(url,login_data,'gb2312')
    if code!=200:
        return False,'network error'
    if re.search('ldap',resp)!=None:
        return False,'infomation error'
    return True,'ok'

# input user's name and password here.
u=''
p=''

#login gate1
code,data_gate1=gethttp('http://10.3.8.216')
if re.search('successfully',data_gate1)==None:
    r1,r2=login_gate1(u,p)
    if r1==True:
        print('logined gate1')
    else:
        print('failed to login gate1',r2)
        sys.exit(1)
else:
    print('gate 1 has been logined already')

#login gate2
code,data_gate2=gethttp('http://10.3.8.211','gb2312')
if re.search('Logout Con',data_gate2)==None:
    r1,r2=login_gate2(u,p)
    if r1==True:
        print('logined gate2')
    else:
        print('failed to login gate2',r2)
        sys.exit(2)
else:
    print('gate 2 has been logined already')
