from django.test import TestCase
from rss.models import (RssURL, 
                        RssFeed, 
                        RssPost)
from members.serializer import MembersSerializer
from rss.serializers import (RssURLSerializer)
from dateutil.parser import parse

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

class RssPostTestCase(TestCase):
    def setUp(self):
        self.test_post={}
        self.test_post['title'] ='this is a post title'
        self.test_post['link'] = 'www.example_post.com'
        self.test_post['pub_date'] = 'Sat 15 Aug 2015 12:00:00'
        self.test_post['description'] = 'This is a post about technology'

        self.test_feed = {
            'link':'www.example.com',
            'title':'this is an example title',
            'description':'This is an example description',
        }

        RssURL.objects.create(url=self.test_feed['link'])
        self.rss_url = RssURL.objects.get(url=self.test_feed['link'])

        RssFeed.objects.create(title = self.test_feed['title'], description= self.test_feed['description'], 
                                                                link = self.test_feed['link'], url= self.rss_url)

        self.rss_feed = RssFeed.objects.get(link=self.test_feed['link'])

        RssPost.objects.create(
                                title = self.test_post['title'], 
                                description= self.test_post['description'], 
                                link = self.test_post['link'], 
                                pub_date = parse(self.test_post['pub_date']),
                                rss_feed=self.rss_feed
                            )

    def test_rss_feed_post_model(self):
        rss_post = RssPost.objects.get(link=self.test_post['link'])
        self.assertEqual(rss_post.link, self.test_post['link'])


            
        
#Test for rss Serializer


class RssURLSerializerTestCase(TestCase):
    def setUp(self):
        membersSerializer = MembersSerializer(data={'email':None, 'password':None})
        if membersSerializer.is_valid():
            self.member =membersSerializer.save()
       
        rssURL_data ={
            'url':'http://example-rss.com/',
        }
        self.serializerURL = RssURLSerializer(data=rssURL_data)
        
        if self.serializerURL.is_valid():
            self.rssURL= self.serializerURL.save()

    def test_rss_url_ser(self):
        data = self.serializerURL.data
        
        rss_ser_next = RssURLSerializer(self.rssURL)
        self.assertEqual(set(data.keys()), set(['url']))
    
    def test_correct_members_added(self):
        member_2_Serializer = MembersSerializer(data={'email':None, 'password':None})

        self.member.rssURLs.add(self.rssURL)
        self.assertEqual(len(self.member.rssURLs.all()),1)


        





        

