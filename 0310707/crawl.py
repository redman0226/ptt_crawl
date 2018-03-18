#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 10:59:03 2018

@author: redman
"""

import numpy as np
import requests
from bs4 import BeautifulSoup
import xml
import urllib.parse
import time
import csv
from requests.exceptions import ConnectionError
def crawl():
    posts =[]
    check=['/bbs/Beauty/M.1490936972.A.60D.html',
           '/bbs/Beauty/M.1494776135.A.50A.html',
           '/bbs/Beauty/M.1503194519.A.F4C.html',
           '/bbs/Beauty/M.1504936945.A.313.html',
           '/bbs/Beauty/M.1505973115.A.732.html',
           '/bbs/Beauty/M.1507620395.A.27E.html',
           '/bbs/Beauty/M.1510829546.A.D83.html',
           '/bbs/Beauty/M.1512141143.A.D31.html'
    ]
    pages =2000
    with open('all_popular.txt','w',encoding='utf-8') as f:
        with open('all_articles.txt','w',encoding='utf-8') as file:
            while (pages !=2353):
                url = 'https://www.ptt.cc/bbs/beauty/index'+str(pages)+'.html'
                try:
                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, 'lxml')
                    for article in soup.find_all(class_='r-ent'):
                
                        meta = article.find(class_= 'title').find('a') 
                        if (meta):
                            posts.append(article.find(class_= 'date').getText())
                            posts.append(meta.getText())
                            posts.append(meta.get('href'))
                            posts.append(article.find(class_='nrec').getText())
                            posts[0]=posts[0].replace('/','').replace(' ','')
                            if (posts[1].find('[公告]')==-1 and posts[2] not in check):
                                #print(posts[1])
                                if(pages==2000 and int(posts[0])<1231):
                                    #print(posts[0])
                                    if(posts[3]=='爆'):
                                        f.write(posts[0]+','+posts[1]+','+'https://www.ptt.cc'+posts[2]+'\n')        
                                    file.write(posts[0]+','+posts[1]+','+'https://www.ptt.cc'+posts[2]+'\n')
                                if(pages==2352 and int(posts[0])>110):
                                    if(posts[3]=='爆'):
                                        f.write(posts[0]+','+posts[1]+','+'https://www.ptt.cc'+posts[2]+'\n')        
                                    file.write(posts[0]+','+posts[1]+','+'https://www.ptt.cc'+posts[2]+'\n')
                                if(pages<2352 and pages>2000):
                                    if(posts[3]=='爆'):
                                        f.write(posts[0]+','+posts[1]+','+'https://www.ptt.cc'+posts[2]+'\n')        
                                    file.write(posts[0]+','+posts[1]+','+'https://www.ptt.cc'+posts[2]+'\n')
                                
                        posts=[]
                    print(pages)
                    pages+=1
            #time.sleep(1)
                except ConnectionError as e:
                    time.sleep(0.5)

        #print(i)










