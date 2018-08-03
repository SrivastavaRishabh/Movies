from django.db import models
import django_filters


# Create your models here


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    birthdate = models.DateField()

    def __str__(self):
        return self.name
    

class Tags(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    slug = models.SlugField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    
class post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tags)
    content = models.TextField()
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    Post = models.ForeignKey(post, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content
    
