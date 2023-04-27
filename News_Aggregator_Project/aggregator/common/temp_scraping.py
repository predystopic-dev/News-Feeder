import datetime
import os
import requests
import shutil
from bs4 import BeautifulSoup as bs
import csv

''' HACKER NEWS
website = "https://news.ycombinator.com/rss"
request = requests.get(website, verify=False)
soup = bs(request.content, 'xml')
for item in soup.channel:
    #print(item.title)
    #print(item.link)
    wp = item.link
    r = requests.get(wp, verify=False)
    soup = bs(r.content, 'html.parser')
    print(soup.title)
'''

website = "https://feeds.feedburner.com/ndtvnews-india-news"
request = requests.get(website, verify=False)
soup = bs(request.content, 'xml')

with open('../../interface/data.csv', 'w') as f:
    fieldnames = ['title', 'image', 'desc', 'pub_date']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for item in soup.find_all('item'):
        title = item.title.text.strip()
        image = item.find('media:content')['url']
        desc = item.description.text.strip()
        pub_date = item.pubDate.text[4:16].strip()
        writer.writerow({'title': title, 'image': image, 'desc': desc, 'pub_date': pub_date})
#print(soup.prettify())

#print(f'{title}\n{image}\n{desc}\n\n')


''' BBC NEWS
website = "http://feeds.bbci.co.uk/news/technology/rss.xml"
request = requests.get(website, verify=False)
soup = bs(request.content, 'xml')
#print(soup.prettify())

for item in soup.find_all('item'):
    title = item.title.text.strip()
    link = item.link.text.strip()
    pub_date = item.pubDate.text.strip()
    desc = item.description.text.strip()
    r = requests.get(link, verify=False)
    inline_soup = bs(r.content, 'html.parser')
    image = inline_soup.find('picture').find('img')['src']
    print(f'{title}\n{image}\n{desc}\n\n')
'''

