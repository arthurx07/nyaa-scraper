#!/bin/env python

from bs4 import BeautifulSoup as bs
import requests
import argparse
import subprocess

parser = argparse.ArgumentParser(description='nyaa.si cli torrent downloader')
parser.add_argument('title', help='title to search')
parser.add_argument(
        '-d', '--download', help='download torrent', action='store_true'
)
args = parser.parse_args()

SAVE = args.download
DOMAIN = 'https://nyaa.si'
URL = 'https://nyaa.si/?f=0&c=0_0&q='+''.join(args.title)


def get_soup(url):
    return bs(requests.get(url).text, 'html.parser')


torrents = ['']
title_list = ['']
for link in get_soup(URL).find_all('a'):
    file_link = link.get('href')
    if '.torrent' in file_link:
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
if SAVE:
    torrent_select = torrents[select_input*2-1]
    title = title_list[select_input]
    with open(f'{title}.torrent', 'wb') as file:
        response = requests.get(DOMAIN + torrent_select)
        file.write(response.content)
    exit(0)

cmd = "/usr/bin/xdg-open {}".format(torrent_select)
p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
