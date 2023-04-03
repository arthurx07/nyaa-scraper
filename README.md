### nyaa-scraper

download nyaa.si torrents from the cli.

    usage: nyaa-scraper [-h] [-e] [-r] [-q] [-g] [-u] [-p] [-s] [-x] [-o] [-l] [-i] title

    nyaa.si cli torrent downloader

    positional arguments:
      title             title to search

    options:
      -h, --help        show this help message and exit
      -e , --episode    specify episode to watch (3|5-8|13,21|-1)
      -r, --rss         track anime with transmission-rss
      -q , --quality    set video quality (best|worst|360|480|720|1080|1440|3840|4k)
      -g , --language   set subtitle language (SPA|ES|ENG|SPA-LA|FRE|GER|etc.)
      -u , --user       set torrent user provider (Erai-raws|DantalianSubs|PuyaSubs!|CameEsp|Ohys-Raws|etc.)
      -p , --path       specify directory to save anime
      -s, --save        download torrent file
      -x, --print       print magnet
      -o , --open       program to open magnet
      -l, --list        list all available torrents and exit
      -i , --input      select torrent number from list (number|sel)
