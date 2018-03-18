#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 10:17:10 2018

@author: redman
"""
import requests
from bs4 import BeautifulSoup
import argparse
import crawl
import push
import popular
import findword
import sys

if __name__ == '__main__':
    
    if(sys.argv[1]=='crawl'):
            #print('boo')
        crawl.crawl()
    if(sys.argv[1]=='push'):
        #print('good')
        push.countpush(sys.argv[2],sys.argv[3])
    if(sys.argv[1]=='popular'):
        popular.countpopular(sys.argv[2],sys.argv[3])
    if(sys.argv[1]=='findword'):
        #print('hello')
        #print(sys.argv[2])
        findword.word(sys.argv[3],sys.argv[4],sys.argv[2])