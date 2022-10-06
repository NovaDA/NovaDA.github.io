import sqlite3
from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup

conn = sqlite3.connect("webscraper.db")
c = conn.cursor()

s = HTMLSession()

number_of_articles = 100
list_of_urls = []
title = []
main_content = []
date = []

page_number_index = 1

while len(list_of_urls) < number_of_articles:
    url = f'https://www.theguardian.com/uk/london?page={page_number_index}'
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    articles_url = doc.find_all(class_='fc-item__container')

    for a in articles_url:
        list_of_urls.append(a.a['href'])
        date.append(" ".join(a.a['href'].rsplit('/', 4)[1:-1]))
        title.append(a.a['href'].rsplit('/', 1)[-1].replace('-', ' '))
        
    page_number_index += 1


#extracted text // following each urls extraceted in step 1

for news in list_of_urls:
    result = requests.get(news)
    doc = BeautifulSoup(result.text, "html.parser")
    articles = doc.find_all(id='maincontent')

    for p in articles:
        art = p.find_all("p")
        body_article = []
        for a in art:   
            body_article.append(a.text)

        main_content.append(" ".join(body_article))


    
c.execute("""CREATE TABLE news (
            article title, 
            text,
            date of article,
            source URL
    )""")

for i in range(0,number_of_articles):
    c.execute("INSERT INTO news VALUES (?, ?, ?, ?)", (title[i], main_content[i], date[i], list_of_urls[i]))
    conn.commit()
    

conn.close()


