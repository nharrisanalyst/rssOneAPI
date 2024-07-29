from rss.serializers import RssFeedSerializer
from feedparser import parse


class Post:
    def __init__(self):
        pass


class RssParser:
    def __init__(self):
       pass
    
    def paresURL(self, url):
        self.url = url
        feed = parse(self.url)
        data = {
            'title':feed.feed.title,
            'description':feed.feed.description,
            'link':feed.feed.link,
            post:[]
        }


    
        