#!/usr/bin/env python
from pyquery import PyQuery as pq

html = '<table>...</table>'
doc = pq(html)

cells = doc('td')

for cell in cells:
    pq(cell).text('new value')
print(doc.html())