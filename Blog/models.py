from django.db import models
from tagging.fields import TagField


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    birthdate = models.DateField()

    def __str__(self):
        return self.name
    

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    # @permalink
    # def get_absolute_url(self):
    #     return ('blog_category_detail', None, {'slug': self.slug})


class Post(models.Model):
    STATUS_CHOICES = (
        (1, 'Draft'),
        (2, 'Public'),
    )
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE)
    body = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)
    created = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, blank=True)
    tags = TagField()
    
    def __self__(self):
        return self.title

    # @permalink
    # def get_absolute_url(self):
    #     return ('blog_detail', None, {
    #         'slug': self.slug
    #     })
