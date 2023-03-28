#imports
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import pandas as pd


#Connect to website

URL = 'https://www.marketwatch.com/investing/stock/tsla'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate, br","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Upgrade-Insecure-Requests": "1"}
page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

price = soup2.find(class_='value').get_text()

price= price.strip()
title = 'TSLA'
date = datetime.date.today()
date_time = time.localtime()
t = time.strftime("%H:%M:%S", date_time)


#Writing data to a csv file

import csv 

header = ['Title', 'Price', 'Date', 'Time']
data = [title,price,date, t]

type(data)

with open('webscraperproject.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    

#Verifying data in csv

df = pd.read_csv(r'C:\Users\poude\webscraperproject.csv')

print(df)


#Appending data to csv
def stock_check():
    URL = 'https://www.marketwatch.com/investing/stock/tsla'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate, br","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Upgrade-Insecure-Requests": "1"}
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
    price = soup2.find(class_='value').get_text()
    price= price.strip()
    title = 'TSLA'
    t = datetime.datetime.now().strftime("%H:%M:%S")
    data = [title,price,date, t]
    type(data)
    with open('webscraperproject.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


while(True):
    stock_check()
    time.sleep(10)





