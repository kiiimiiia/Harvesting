import mysql.connector
import requests
from bs4 import BeautifulSoup
import re
db = mysql.connector.connect(user='root', password='maSliD@1372',
                              host='127.0.0.1',
                              database='test')
# cnx.close()
mycursor = db.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
session = requests.Session()

session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'})
r = session.get('http://forum.dataak.com/member.php')
# pprint(r.content.find())
soup = BeautifulSoup(r.content , 'html.parser')
script = soup.select('script').__str__()
# key = re.findall(r'my_post_key = [a-zA-Z0-9]',str(script).__str__())
response = session.post('http://forum.dataak.com/member.php' , data = {'action':'do_login' ,
                                                                       'url': 'http://forum.dataak.com/index.php',
                                                                       'quick_login ':'1' ,
                                                                       'my_post_key': script.split('my_post_key')[1].split('"')[1].__str__() ,
                                                                       'quick_username': 'maryam',
                                                                       'quick_password': '@123456',
                                                                       'quick_remember': 'yes',
                                                                       'submit' : 'ورود'
                                                                       })
print(response.status_code)
response2 = session.get('http://forum.dataak.com/index.php')
print(response2.status_code)
soup = BeautifulSoup(response2.content , 'html.parser')
soup = BeautifulSoup( soup.find("div", {"id": "content"}).__str__() , 'html.parser')
ref = soup.select('table tbody td strong a')
print(ref)
baseUrl = 'http://forum.dataak.com/'
url = []
for el in ref:
    url.append(re.findall(r'"([^"]*)"', el.__str__()))
    main_forum = re.findall(r'>([^"]*)<', el.__str__())
    sql = "INSERT INTO forum (name) VALUES (%s)"
    val = (main_forum)
    mycursor.execute(sql, val)

    db.commit()


    # for el in ref:
    # print(.split('>'))
# print(forums)
# print(ref)
# ref = soup.select('a').__str__()
# ref = ref.split(" ")
# # print(ref)
# links = []
# x = 0
# for el in ref :
#     if el == '<a':
#         if len(ref[x+1])> 18 and ref[x+1][0:18] == 'href="forumdisplay':
#             links.append(ref[x+1].split('"')[1])
#
#     x+=1
# print(links)


session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'})
#
# for link in links :
#     print(baseUrl+link)
#     res = session.get(baseUrl+link)
#     print(res.content)
#










# print(re.findall('^href="forumdisplay' , ref))
# print(response2)
# soup = BeautifulSoup(response.content , 'html.parser')
# print (soup.select('a,href'))
# r = session.get('http://forum.dataak.com/member.php')
#
# r = session.post('http://forum.dataak.com/member.php')
# print(r.headers)

# r = requests.get('http://forum.dataak.com/member.php')
#
# r = requests.post('http://forum.dataak.com/member.php', data = {'action':'do_login' ,
#                                                                 'url': 'http: // forum.dataak.com /',
#                                                                'quick_login ':'1'  ,
#                                                                'my_post_key': '02fd169ef8ad724bb2e594e39d001ae1' ,
#                                                                'quick_username': 'maryam',
#                                                                'quick_password': '@123456' ,
#                                                                'quick_remember': 'yes' ,
#                                                                'submit' : 'ورود'
#                                                                 })
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
# r = requests.get('http://forum.dataak.com/member.php', headers=headers)
#
# r = requests.get('http://forum.dataak.com/index.php' )
# soup = BeautifulSoup(r.content , 'html.parser')
# print (soup.select('a,href'))


# print(r.content)
# r.text
# r.content
# r.json()
# r.raw
# r.status_code
# r.headers
# r.cookies['example_cookie_name']

# action: do_login
# url: http://forum.dataak.com/
# quick_login: 1
# my_post_key: 02fd169ef8ad724bb2e594e39d001ae1
# quick_username: 12312
# quick_password: 12324
# quick_remember: yes
# submit: ورود

#
# jar = requests.cookies.RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# r = requests.get('http://forum.dataak.com/member.php', cookies=jar)

# session = requests.Session()
# session.headers.update({'User-Agent': "myapp1,0"})
# mydata = json.dumps({'username': username,'password': password})
# response = session.post(loginurl,data=mydata)
# session.get(followingurl)
# session.post(followingurl)
# with open('cookiefilename', 'w') as f:
#     json.dump(requests.utils.dict_from_cookiejar(session.cookies), f)




# username = 'myuser'
# password = 'mypassword'
#
# cj = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# login_data = urllib.urlencode({'username' : username, 'j_password' : password})
# opener.open('http://www.example.com/login.php', login_data)
# resp = opener.open('http://www.example.com/hiddenpage.php')
# print resp.read()
