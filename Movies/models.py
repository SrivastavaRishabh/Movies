from django.db import models
from django.db.models import permalink
from django.conf import settings


# Create your models here.
class Genre(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('title',)
    
    def __str__(self):
        return self.title
        
       
class Studio(models.Model):
    title = models.CharField(max_length=100)
    prefix = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    web = models.URLField(blank=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return '%s %s' % (self.prefix, self.title)


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10, null=True, blank=True)
    website = models.URLField(blank=True)

    class Meta:
        ordering = ('first_name',)
    
    def __str__(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    prefix = models.CharField(max_length=20, blank=True)
    subtitle = models.CharField(blank=True, max_length=100)
    slug = models.SlugField(unique=True)
    directors = models.ManyToManyField(Director, related_name="Movies")
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, related_name="Movies")
    released = models.DateField()
    asin = models.CharField(blank=True, max_length=100)
    coverimage = models.FileField(upload_to='images/')
    review = models.TextField(max_length=100)
    genre = models.ManyToManyField(Genre, related_name="Movies")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('title',)
    




    




