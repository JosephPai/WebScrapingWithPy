#伪装浏览器访问
import requests
from bs4 import  BeautifulSoup
import  re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
web_url = 'https://unsplash.com'
r = requests.get(web_url, headers=headers)
print(r.text)
all_a = BeautifulSoup(r.text,'lxml').find_all('a', title = re.compile('View the'))
print(all_a)
# for a in all_img:
#     print(a['src'])