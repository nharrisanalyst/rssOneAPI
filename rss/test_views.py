from rest_framework.test import APITestCase
from rest_framework import status
from members.models import Members
from rss.models import RssURL
from rss.views import message_created


class RssURLTestCase(APITestCase):
    def test_rss_post(self):
        data ={'member':"1", "url":"http://example-rss.com/"}
        response = self.client.post('/api/rssurl',data, format='json')
        return_data = response.data
        self.assertEqual(return_data['message'], message_created)
        self.assertEqual(len(RssURL.objects.all()),1)
        self.assertEqual(set(return_data.keys()), set(['message', 'feed']))
        self.assertEqual(set(return_data['feed'].keys()), set(['url','title', 'link', 'description','post']))
        


