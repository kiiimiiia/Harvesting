import mysql.connector
import requests
from bs4 import BeautifulSoup
import re

class posts:
  def __init__(self, username, title, forum):
    self.username = username
    self.title == title
    self.forum = forum

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
# print(response2.status_code)
soup = BeautifulSoup(response2.content , 'html.parser')
soup = BeautifulSoup( soup.find("div", {"id": "content"}).__str__() , 'html.parser')
ref = soup.select('table tbody td strong a')
# print(ref)
baseUrl = 'http://forum.dataak.com/'
urls = []
forums = []
i = 0
for el in ref:
    urls.append(re.findall(r'"([^"]*)"', el.__str__())[0])
    forums.append(re.findall(r'>([^"]*)<', el.__str__())[0] )
#
# print(urls)
# print(forums)



""" collecting profile urls """
response_members = session.get("http://forum.dataak.com/memberlist.php")
soup2 = BeautifulSoup(response_members.content, 'html.parser')
ref2 = soup2.select('tr td a')
# print(ref2)
profile_urls = []
usernames = []
for el in ref2:
    url_temp = ""
    username = ""
    url_temp = re.findall(r'"([^"]*)"', el.__str__())[0]
    username = re.findall(r'>([^"]*)<', el.__str__())[0]
    if(username == ''):
        username = re.findall(r'>([^"]*)<', soup2.select('span strong em')[0].__str__())[0]
    if ("http://forum.dataak.com/member.php?action=profile&amp;" in url_temp):
        profile_urls.append(url_temp)
        usernames.append(username)
#
# print(profile_urls)
# print(usernames)

j = 0
"""collecting user infos"""

for profile_url in profile_urls:
    profile_response = session.get(profile_url)
    soup2 = BeautifulSoup(profile_response.content, 'html.parser')
    # soup2 = BeautifulSoup(soup.find("fieldset").__str__(), 'html.parser')
    temp = []
    temp = soup2.select('tr td span.smalltext')
    # print(temp)
    birth_date = ""
    registry_date=""
    for el in temp :
        if(len(el.__str__())>40):
            registry_date = el.__str__().split('<br/>')[3].split('</strong>')[1].split('<strong>')
            birth_date = el.__str__().split('<br/>')[4].split('</strong>')[1].split('<strong>')

    sql = "INSERT INTO user (user_name , registry_date , birth_date) VALUES (%s,%s,%s)"
    val = (usernames[j] ,registry_date[0] ,birth_date[0])
    try:
        mycursor.execute(sql, val)
    except:
        print("duplicate username")
    j+=1
db.commit()

i = 0
for url in urls:
    forum_url = baseUrl + url
    f_response = session.get(forum_url)
    soup2 = []
    soup2 = BeautifulSoup(f_response.content, 'html.parser')
    ref2 = []
    ref2 = soup2.select('tr td strong a')

    # sub forums
    for el in ref2:
        url_temp = ""
        forums_temp = ""
        url_temp  = re.findall(r'"([^"]*)"', el.__str__())[0]
        forums_temp = re.findall(r'>([^"]*)<', el.__str__())[0]
        if (("forumdisplay.php?fid=" in url_temp ) and len(url_temp) <= 25):
            urls.append(url_temp)
            forums.append(forums_temp)

    soup2 = BeautifulSoup(f_response.content, 'html.parser')
    posts_pages = soup2.select('tr.inline_row td.trow1.forumdisplay_regular div span span.smalltext a')
    print(posts_pages)
    posts = soup2.select('tr.inline_row td.trow1.forumdisplay_regular div span span.smalltext a')
    # soup2 = BeautifulSoup(f_response.content, 'html.parser')
    # ref2 = []
    # ref2 = soup2.select('tr td strong a')
    # main_forum = re.findall(r'\'([^"]*)\'', forum[0].__str__())
    # print(main_forum)
    # sql = "INSERT INTO forum (name) VALUES (%s)"
    # val = (main_forum)
    # mycursor.execute(sql, val)
    #
    # refs = soup2.select('tbody td strong a')
    # print(refs)
    # main_forum = re.findall(r'>([^"]*)<', refs.__str__())

print(forums)

# db.commit()
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
