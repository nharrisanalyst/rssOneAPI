from django.db import models
from members.models import Members
from django.utils.timezone import now

# Create your models here.

class RssURL(models.Model):
    url = models.URLField(max_length=2000, unique=True)
    members = models.ManyToManyField(to=Members)


class RssFeed(models.Model):
    url = models.ForeignKey(RssURL, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    link = models.URLField(max_length=2000)
    description = models.CharField(max_length=100)


class RssPost(models.Model):
    rss_feed = models.ForeignKey(RssFeed, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    link = models.URLField(max_length=2000)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=now)
    description = models.CharField(max_length=1000)


