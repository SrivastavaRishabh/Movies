from django.db import models
from tagging.fields import TagField

class Bookmarks(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    description = models.CharField(max_length=100)
    tags = TagField()
    
    def __str__(self):
        return self.name
    