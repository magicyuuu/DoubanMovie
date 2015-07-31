# -*- coding: UTF-8 -*-
__author__ = 'yushiwei'

import urllib2
import urllib
import json
import printer

API = '01068bdd0c3168a70313a397249439f5'

def searchMovie(query, timeout=5):
    if query is None or query == '':
        return {}
    response = urllib2.urlopen(url='https://api.douban.com/v2/movie/search?apikey=%s&q=%s' % (API, urllib.quote(query)))
    if response.getcode() == 200:
        data = json.load(response)
        return data
    return {}

def showMovie(data):
    p = printer.Printer()
    if data is None or data == {} or data['subjects'] == []:
        p.add_item(title='没找到...')

    for movie in data['subjects']:
        if movie['title'] != movie['original_title']:
            title = '%s %s' % (movie['title'], movie['original_title'])
        else:
            title = movie['title']
        actors = []
        subtitle = '年份:%s 评分:%s 演员:%s' % (movie['year'], movie['rating']['average'], '/'.join(actors))
        arg = '{"title": %s, "original_title:" %s}'

        p.add_item(title=title, subtitle=subtitle, arg=arg, valid=True, icon='')
    p.sendToWorkFlow()