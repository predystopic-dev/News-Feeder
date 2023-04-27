from ...models import Article
import datetime
from django.core.management.base import BaseCommand
import subprocess
#from ....aggregator.common.temp_scraping import scraper_function


class Command(BaseCommand):
    help = 'Scrapes news from a website'

    def handle(self, *args, **options):
        print("Scraping news from a website")
        #subprocess.Popen([scraper_function()])
