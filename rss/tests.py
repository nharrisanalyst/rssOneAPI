from django.test import TestCase
from rss.models import RssURL

# Create your tests here.

#Test for Models

class RssUrlTestCase(TestCase):
    def setUp(self):
        self.test_url = 'http://example.com/'
        RssURL.objects.create(url=self.test_url)

    def test_there_is_an_email(self):
        RssURL.objects.get(url=self.test_url)
