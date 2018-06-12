
# coding: utf-8

# In[1]:

import urllib
import cssselect
from lxml.html import fromstring
from pandas import DataFrame
from urllib import urlopen
from lxml.etree import XMLSyntaxError
import csv


# In[2]:

#constants
URL_rns = 'https://rns.online/society/'
ITEM_PATH_rns = '.b-list__container .b-list__time-slice .b-list__items'
IN_ITEM_PATH_rns = '.b-news .t-body'


# In[3]:

def parse_news_rns():
    #clear()
    #import_from_csv()
    f = urlopen(URL_rns)
    list_html = f.read().decode('utf-8')
    list_doc = fromstring(list_html)
    for elem in list_doc.cssselect(ITEM_PATH_rns):
        a = elem.cssselect('a')[0]
        header = a.text
        href = a.get('href')
        if 'http' in href:
            continue
        real_href = 'https://rns.online' + href

        header_row_rns.update({real_href:header})
        information = urlopen(real_href).read().decode('utf-8')
        try:
            news = fromstring(information)
        except XMLSyntaxError:
            continue
        descr_news = news.cssselect(IN_ITEM_PATH_rns)
        text = list()
        for part in descr_news:
            for i in range(10):
                try:
                    p = part.cssselect('p')[i]
                    row = p.text_content()
                    if row != None:
                        text.append(row)
                except IndexError:
                    continue


# In[ ]:



