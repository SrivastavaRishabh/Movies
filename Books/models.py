from django.db import models
import django_filters
# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __str__(self):
       return '%s %s' % (self.first_name, self.last_name)

class Genre(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Books(models.Model):
    name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    pages = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    pubdate = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name