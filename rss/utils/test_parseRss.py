from django.test import TestCase
from rss.utils.parseRss import RssParser

rss_url = 'http://elijahmeeks.com/rss.xml'

class ParseURLTest(TestCase):
    def setUp(self):
        self.parser = RssParser()
    
    def test_parse_url(self):
        rss_data = self.parser.paresURL(rss_url)

        self.assertEqual(rss_data.title, 'Elijah Meeks')
        self.assertEqual(rss_data.description, 'Articles by Elijah Meeks about data visualization and analysis')
        self.assertEqual(rss_data.link, 'http://elijahmeeks.com/#blog')

        self.assertGreater(len(rss_data.posts),0)
        self.assertIn('title', rss_data.posts[0].__dir__())

    
