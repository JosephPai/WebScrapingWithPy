# 把“贝肯数”（一个页面与凯文·贝肯词条页面的链接数）不超过 6 的维基百科页面存储起来
from bs4 import BeautifulSoup
import re
import pymysql
from urllib.request import urlopen

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='06104777', db='mysql', charset='utf8')

cur = conn.cursor()
cur.execute("USE wikipedia")

def insertPageIfNotExists(url):
    cur.execute("SELECT * FROM pages WHERE url = %s",(url))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO pages(url) VALUES(%s)",(url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]

def insertLink(fromPageId, toPageId):
    cur.execute("SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s",(int(fromPageId),int(toPageId)))
    conn.commit()
    if cur.rowcount == 0:
        cur.execute("INSERT INTO links (fromPageId, toPageId) VALUES (%s,%s)",(int(fromPageId),int(toPageId)))
        conn.commit()

pages = set()
def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return ;
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if link.attrs['href'] not in pages:
            # 遇到一个新页面，加入集合并搜索里面的词条链接
            newPage = link.attrs['href']
            pages.add(newPage)
            getLinks(newPage,recursionLevel+1)
getLinks("/wiki/Kevin_Bacon",0)
cur.close()
conn.close()