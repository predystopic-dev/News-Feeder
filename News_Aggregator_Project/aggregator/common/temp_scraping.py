import datetime
import os
import requests
import shutil
from bs4 import BeautifulSoup as bs
import csv
from aggregator.models import Article

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

# with open('interface/data.csv', 'w') as f:
#     fieldnames = ['title', 'image', 'desc', 'pub_date']
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     for item in soup.find_all('item'):
#         title = item.title.text.strip()
#         image = item.find('media:content')['url']
#         desc = item.description.text.strip()
#         pub_date = item.pubDate.text[4:16].strip()
#         writer.writerow({'title': title, 'image': image, 'desc': desc, 'pub_date': pub_date})
#print(soup.prettify())

#print(f'{title}\n{image}\n{desc}\n\n')

for item in soup.find_all('item'):
    headline = item.title.text.strip()
    image = item.find('media:content')['url']
    desc = item.description.text.strip()
    pub_date = item.pubDate.text[4:16].strip()
    url = item.link.text.strip()
    r = requests.get(url, verify=False)
    full_article = bs(r.content, 'html.parser')
    metadata_div = full_article.find('div', class_='pst-by_ul')
    author_name = metadata_div.find('span', itemprop='author').find('span', itemprop='name').text.strip()
    tag = full_article.find('span', class_='pst-by_li').text.strip()
    #article_div = bs(r.content, 'html.parser').find('div', id='ins_storybody')
    location = full_article.find('div', id='ins_storybody').find('b', class_='place_cont').text.strip()
    body = ""
    for p in full_article.find('div', id='ins_storybody').find_all('p'):
        body += p.text.strip()
    #print(f'{headline}\n{image}\n{desc}\n{pub_date}\n{url}\nauthor name: {author_name}\n{location}\n{body}\n\n')
    article = Article(headline=headline, author_name=author_name, url=url, pub_date=pub_date, image=image, body=body, bias_score=bias_score, tag=tag, location=location)
    article.save()



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

