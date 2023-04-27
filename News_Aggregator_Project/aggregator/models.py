from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    headline = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    url = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    news_icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    bias_score = models.FloatField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
'''
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
'''