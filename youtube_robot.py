#import the webscrapping libraries

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs
import re
from selenium import webdriver
import pandas as pd
import time
import io

# driver = webdriver.Chrome('C:/chromedriver/chromedriver')
# page = 'https://www.youtube.com/watch?v=3wgsJj_l2a4&list=PLHhi9ctsSYvWMpEMSzALrDmR2Dr3CHbI4'
#
# driver.implicitly_wait(30)
# driver.get(page)
#
# soup_head=bs(driver.page_source, 'html.parser')
#
# containers = soup_head.find_all("a",{"id":"wc-endpoint"})
# print(len(containers))





def keyword_puller(url_page):

    client = uReq(url_page)
    page_html = client.read()
    client.close()

    # creating the Regex
    pattern2 = re.compile(r'"keywords":"(.*?)"')

    # coverting to Soup object
    page_bs = bs(page_html, "html.parser")


    # pulling out the keywords
    keys = page_bs.find("script",text=pattern2)
    if keys:
        match = pattern2.search(keys.text)
        if match:
            keywords = match.group(1)
            return(keywords)

links = pd.read_table('E:/R files/jenn_stuff/videolist.txt', header=None)
#links2 = links.values
print(len(links))

filename = 'E:/R files/jenn_stuff/keywords.csv'
f = io.open(filename, "w", encoding="utf-8")
headers = 'keywords:  \n'

f.write(headers)

for i in range(0,len(links)):
    out = keyword_puller(links[0][i])
    time.sleep(5)
    #writing keywords out to a file
    f.write(out.replace(",","|") + "\n")

f.close()