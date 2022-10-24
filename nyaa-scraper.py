#!/bin/env python

from bs4 import BeautifulSoup as bs
import requests
import sys
import subprocess

DOMAIN = 'https://nyaa.si'
URL = 'https://nyaa.si/?f=0&c=0_0&q='+''.join(sys.argv[1:])
FILETYPE = '.torrent'


def get_soup(url):
    return bs(requests.get(url).text, 'html.parser')


torrents = ['']
title_list = ['']
for link in get_soup(URL).find_all('a'):
    file_link = link.get('href')
    if FILETYPE in file_link:
        torrents.append(file_link)

for i in torrents[2::2]:  # return only even indices of a list
    j = i.split('&dn=')
    k = j[1]
    k = k.split('&tr=')
    title = k[0]
    title = requests.utils.unquote(title)
    title_list.append(title)

for (i, item) in enumerate(title_list[1:], start=1):
    print(i, item)

select_input = int(input('\nEnter torrent to download: '))
torrent_select = torrents[select_input*2]

cmd = "/usr/bin/xdg-open {}".format(torrent_select)
p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)

# to do:
# convert filename to readable text --> use a UTF-8 convertor or smth
# let user decide to download torrent or open magnet
# implement fzf
