#!/usr/bin/env python

import urllib.request
url = 'http://frp.4hotel.tw:24480/index.html'

with urllib.request.urlopen(url) as response:
   html = response.read()

print("Content-Type: text/html")
print()
print(html)