#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 14:49:56 2018

@author: redman
"""
import sys
import numpy as np
import requests
from bs4 import BeautifulSoup
import xml
import urllib.parse
import time
import csv
from requests.exceptions import ConnectionError

def countpush(start_date, end_date):
    idlist_push={}
    idlist_boo={}
    idlist={}
    idlist_b={}
    all_posts= []
    all_post=[]
    n=0
    push_num=0
    boo_num=0
    push_max=0
    push_min=0
    with open('all_articles.txt','r',encoding='utf-8') as f:
        all_posts.append ([line.strip().split(',') for line in f])
        #all_post[n]=np.asarray(all_posts[0][0])
    for item in all_posts[0]:
    
        if (int(item[0])>=int(start_date) and int(item[0])<=int(end_date)):
            n+=1
            url=item[-1] 
            #url='https://www.ptt.cc/bbs/Beauty/M.1483249659.A.63C.html'
            print (n)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            #print(soup.find_all(class_='bbs-screen bbs-content'))
            for test in soup.find_all(class_='bbs-screen bbs-content'):
                flag=False
                tes=test.find(class_='f2')
                for content in test.find_all(class_='push'):
                        boo = content.find(class_='f1 hl push-tag')
                        push = content.find(class_='hl push-tag')
                        if(content.find(class_='f3 hl push-userid') is not None):
                            idname = content.find(class_='f3 hl push-userid').getText()
                #print(push)
                        if(idlist_push.__contains__(idname)!=True):
                            idlist_push[idname]=0
                        if(idlist_boo.__contains__(idname)!=True):
                            idlist_boo[idname]=0
                        if( push is not None and push.getText()=="推 "):
                            #if(idlist.__contains__(idname)!=True):
                             #   idlist[idname]=0
                             push_num+=1
                             idlist_push[idname]+=1 
                                #print(push_num)
                        if( boo is not None and boo.getText()=="噓 "):
                            #if(idlist_b.__contains__(idname)!=True):
                             #   idlist_b[idname]=0
                             boo_num+=1
                             idlist_boo[idname]+=1
        #idlist.clear()
        #idlist_b.clear()
    rank_push=sorted(idlist_push.items(), key=lambda x:x[1],reverse=True)
    rank_boo=sorted(idlist_boo.items(), key=lambda x:x[1],reverse=True)
    with open('push['+start_date+'-'+end_date+'].txt','w') as o:
        o.write('all like: '+str(push_num)+'\n')
        o.write('all boo: '+str(boo_num)+'\n')
        for i in range(10):
            o.write('like #'+str(i+1)+': '+rank_push[i][0]+' '+str(rank_push[i][1])+'\n')
        for i in range(10):
            o.write('boo #'+str(i+1)+': '+rank_boo[i][0]+' '+str(rank_boo[i][1])+'\n')
    #print(rank_push[0:10])
    
    
if __name__ == '__main__':
    #start_date=sys.argv[1]
    #end_date=sys.argv[2]
    countpush('101','101')
    