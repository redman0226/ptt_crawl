#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 19:53:43 2018

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

def countpopular(start_date, end_date):
    names=['.png','.PNG','.jpg','.JPG','.jpeg','.JPEG','.gif','.GIF','.jPg']
    all_popular= []
    image_all=[]
    popular_num=0
    with open('all_popular.txt','r',encoding='utf-8') as f:
        all_popular.append ([line.strip().split(',') for line in f])
        
    for item in all_popular[0]:
    
        if (int(item[0])>=int(start_date) and int(item[0])<=int(end_date)):
            popular_num+=1
            url=item[-1] 
            #print(url)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            for images in soup.find(class_='bbs-screen bbs-content').find_all('a'):
                image=images.getText()
                for name in names:
                    if(image.find(name,-4)!=-1):
                        image_all.append(image)
    #print(image_all) 
    with open('popular ['+start_date+'-'+end_date+'].txt','w') as file:
        file.write('number of popular articles: '+str(popular_num)+'\n')
        for image in image_all:
            file.write(image+'\n')
            
if __name__ == '__main__':
    start_date=sys.argv[1]
    end_date=sys.argv[2]
    countpopular(start_date,end_date)