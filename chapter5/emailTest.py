import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

def sendMail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = "An Email Alert"
    msg['From'] = "ustb2015bzch@163.com"
    msg['To'] = "784161972@qq.com"
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"))
while(bsObj.find("a",{"id":"answer"}).attrs['title']=="NO"):
    print("It is not Christmas yet.")
    time.sleep(3600)
bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"))
sendMail("It's Christmas!", "According to http://itischristmas.com, it is Christmas!")

# 这个程序每小时检查一次 https://isitchristmas.com/ 网站（根据日期判断当天是不是圣诞
# 节）。如果页面上的信息不是“NO”（中国用户在网站页面上看到的“NO”在源代码里是
# <noscript> 不是 </noscript>），就会给你发一封邮件，告诉你圣诞节到了