# -*- coding: utf-8 -*-
"""WebScraping-SankhyaTM

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14p7HURCc94DF4RsG0TiVAVzRKs629Pcr
"""

pip install beautifulsoup4

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re


url = "http://www.abrasem.com.br/abc-agricultura-e-pecuaria-s-a/"
try:
    html = urlopen(url)
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(),"html.parser")
    '''tags = res.findAll(re.compile("CEP"))
    
    print(tags)
    for tag in tags:
        lista = tag.get_text()
        print(tag.name)'''
    for tag4 in res.find_all(re.compile("CEP")):
      print(tag4.get_text)

