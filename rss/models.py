from django.db import models
from members.models import Members

# Create your models here.

class RssURL(models.Model):
    url = models.URLField(max_length=2000)
    members = models.ManyToManyField(Members)


class RssData(models.Model):
    url = models.ForeignKey(RssURL, on_delete=models.CASCADE)