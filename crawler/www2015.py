#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# Copyright (c) 2017 - xiongjiezk <xiongjiezk@163.com>



import re
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = r'href="(.+?p[0-9]+\.pdf)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist

def getFileName(html):
    reg = r'none\">\w+[\w\s\.\,\:\-]+\w+<\\a>$'
    filere = re.compile(reg)
    fileList = re.findall(filere, html)
    return fileList

html = getHtml("http://www2015.wwwconference.org/documents/proceedings/forms/proceedings.htm")
print getImg(html)
print getFileName(html)
