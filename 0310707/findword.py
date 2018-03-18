#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 22:16:56 2018

@author: redman
"""
import sys
import requests
from bs4 import BeautifulSoup
import xml
import urllib.parse
import time
import csv
from requests.exceptions import ConnectionError

def word(start_date, end_date,key):
    names=['.png','.PNG','.jpg','.JPG','.jpeg','.JPEG','.gif','.GIF','.jPg']
    all_popular= []
    content_all=[]
    popular_num=0
    image_all=[]
    with open('all_articles.txt','r',encoding='utf-8') as f:
        all_popular.append ([line.strip().split(',') for line in f])
        
    for item in all_popular[0]:
    
        if (int(item[0])>=int(start_date) and int(item[0])<=int(end_date)):
            popular_num+=1
            url=item[-1] 
            #url='https://www.ptt.cc/bbs/Beauty/M.1484453927.A.CF0.html'
            #print(url)
            #image_all.append(item[-1])
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            #print(soup.find('div',class_='bbs-screen bbs-content'))
            for contents in soup.find_all('div',class_='bbs-screen bbs-content'):
                '''
                try:
                    content=contents.getText()
                    if content.find('※ 發信站')!=-1:
                        break
                    if content:
                        content_all.append(content)
                except:
                    cont=contents.strip()
                    cont=cont.strip('--')
                    if cont:
                        content_all.append(cont)
                '''
                #print(contents)
                content=str(contents).split('※ 發信站')[0]
                #print(content)
                #or element in content_all:
                #print(content_all)
                if (content.find(key)!=-1):
                    #image_all.append(item[-1])
                 #   print(item[-1])
                    for images in soup.find(class_='bbs-screen bbs-content').find_all('a'):
                        image=images.getText()
                        #print(image)
                        for name in names:
                            if(image.find(name,-4)!=-1):
                                #if(not (image in image_all)):
                                image_all.append(image)
                                #print(image)
                               # break
                        
    #print(content_all)
    with open('keyword('+key+')['+start_date+'-'+end_date+'].txt','w') as file:
        for image in image_all:
            file.write(image+'\n')
            
if __name__ == '__main__':
    #key= sys.argv[1]
    #start_date=sys.argv[2]
    #end_date=sys.argv[3]
    word('101','101','正妹')