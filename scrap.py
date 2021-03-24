#! /usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import psycopg2
import os
import logging

logging.basicConfig(filename='scrap_log.txt', level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

url='https://wikileaks.org'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

def insertInBdd(values):
    conn = psycopg2.connect(database="scraptest", user="postgres" , password="pw123" , host="52.176.157.167")
    logging.info("[BDD] Successfully connected to your database")
    mycursor = conn.cursor()
    val = values
    sql = "INSERT INTO articles (title,image,content,date) values (%s,%s,%s,%s)"
    mycursor.execute(sql,val)
    conn.commit()
    logging.info("[BDD]insert into the database success !")
    return str(mycursor) + "nouvelle entree"


def getArticle():
    url='https://wikileaks.org'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    article_main = soup.find_all('li', class_="tile")

    article_titles = []
    article_dates = []
    article_contents = []
    article_images = []
    articles = [article_titles,article_images,article_contents,article_dates]
    

    for article in article_main:
        article_title = article.h2.text
        article_img ="http://wikileaks.com" + article.img.attrs['src']
        article_date = article.find('div',class_='timestamp').text
        article_content = article.p.text
        insertInBdd([article_title,article_img,article_content, article_date])

getArticle()
