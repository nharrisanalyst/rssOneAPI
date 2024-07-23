from django.test import TestCase
from rss.models import (RssURL, 
                        RssFeed)

# Create your tests here.

#Test for Models

class RssUrlTestCase(TestCase):
    def setUp(self):
        self.test_url = 'http://example.com/'
        RssURL.objects.create(url=self.test_url)

    def test_there_is_an_email(self):
        rss_url = RssURL.objects.get(url=self.test_url)
        self.assertEqual(rss_url.url, self.test_url)


class RssFeedTestCase(TestCase):
    def setUp(self):
        self.test_feed = {
            'link':'www.example.com',
            'title':'this is an example title',
            'description':'This is an example description',
        }
        RssURL.objects.create(url=self.test_feed['link'])
        self.rss_url = RssURL.objects.get(url=self.test_feed['link'])

        RssFeed.objects.create(title = self.test_feed['title'], description= self.test_feed['description'], 
                                                                link = self.test_feed['link'], url= self.rss_url)

    def test_rss_feed_model(self):
        rss_feed = RssFeed.objects.get(link=self.test_feed['link'])
        self.assertEqual(rss_feed.link, self.test_feed['link'])

        

