#!/usr/bin/python
import os

from bs4 import BeautifulSoup
CAT_XPATH = '.category-header  h3'

with open('compe.html', 'r') as f:

    contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')
    mes_cat = soup.select(CAT_XPATH)
    for cat in mes_cat:
        os.system("mkdir challenges/{}".format(cat.text))
