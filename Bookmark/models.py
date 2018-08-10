from django.db import models
from taggit.managers import TaggableManager


class Bookmarks(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    description = models.CharField(max_length=100)
    tags = TaggableManager()

    def __str__(self):
        return self.name
