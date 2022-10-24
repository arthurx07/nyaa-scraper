#!/bin/env python

from bs4 import BeautifulSoup as bs
import requests
import sys

DOMAIN = 'https://nyaa.si'
URL = 'https://nyaa.si/?f=0&c=0_0&q='+''.join(sys.argv[1:])
FILETYPE = '.torrent'


def get_soup(url):
    return bs(requests.get(url).text, 'html.parser')


for link in get_soup(URL).find_all('a'):
    file_link = link.get('href')
    if FILETYPE in file_link:
        print(file_link)
