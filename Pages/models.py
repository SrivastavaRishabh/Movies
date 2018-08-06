from django.db import models
from django.utils.text import slugify
# Create your models here.


class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    html_content = models.TextField()
    order = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'id']
    
    def __str__(self):
        return self.title


