from rss.serializers import RssFeedSerializer
from feedparser import parse


class Feed:
    def __init__(self, title, description, link, lastBuildDate, posts):
        self.title = title
        self.description = description
        self.link  = link
        self.posts = posts
        self.lastBuildDate = lastBuildDate

class Post:
    def __init__(self, link, title, description, pubDate):
        self.link = link
        self.title = title
        self.description = description
        self.pubDate = pubDate


class RssParser:
    def __init__(self):
       pass
    
    def paresURL(self, url):
        self.url = url
        feed = parse(self.url)

        posts = []

        for post in feed.entries:
            title = post.title
            description = post.description
            link = post.link
            pubDate = post.published_parsed
            posts.append(Post(link=link, title=title, description=description, pubDate=pubDate))

        return Feed(title=feed.feed.title, description=feed.feed.description, link=feed.feed.link, lastBuildDate = feed.feed.get('lastBuildDate', None), posts=posts)
        


    
        