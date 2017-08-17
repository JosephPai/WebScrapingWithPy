from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest
from urllib.parse import unquote
import re
import random

class TestWikipedia2(unittest.TestCase):
    bsObj = None
    url = None

    def test_PageProperties(self):
        global bsObj
        global url

        url = "http://en.wikipedia.org/wiki/Monty_Python"
        # 测试遇到的前100个页面
        for i in range(1,100):
            bsObj = BeautifulSoup(urlopen(url).text())
            titles = self.titleMatchesURL()
            self.assertEqual(titles[0], titles[1])
            self.assertTrue(self.contentExists())
            url = self.getNextLink()
        print("Done!")

    def titleMatchesURL(self):
        global bsObj
        global url
        pageTitle = bsObj.find("h1").get_text()
        urlTitle = url[(url.index("/wiki/")+6):]
        urlTitle = urlTitle.replace("_"," ")
        urlTitle = unquote(urlTitle)
        return [pageTitle.lower(), urlTitle.lower()]

    def contentExists(self):
        global bsObj
        content = bsObj.find("div",{"id":"mw-content-text"})
        if content is not None:
            return True
        return False

    def getNextLink(self):
        global bsObj
        links = bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
        return links[random.randint(0, len(links)-1)].attrs["href"]

if __name__ == '__main__':
    unittest.main()