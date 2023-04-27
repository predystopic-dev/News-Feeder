import datetime
import os # for making directories
import requests # for making HTTP requests
import shutil # for copying files
#import bs4 as bs # for parsing HTML
from bs4 import BeautifulSoup as bs
from django.contrib.auth.models import User
from models import Article


user = User.objects.get(username='example_user')
website_name = "https://www.bbc.com/news/world/asia/india"
headline = ""
author_name = ""
url = ""
pub_date = datetime.datetime
image = ""
news_icon = ""
body = ""
bias_score = 0.0

article = Article(headline=headline, author_name=author_name, url=url, pub_date=pub_date, image=image, news_icon=news_icon, body=body, bias_score=bias_score, user=user)
article.save()
# Connect to the URL