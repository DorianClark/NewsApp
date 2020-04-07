import datetime
from django.db import models
from django.utils import timezone

class Story(models.Model):
    headline_text = models.CharField(max_length=100)
    story_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.headline_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
