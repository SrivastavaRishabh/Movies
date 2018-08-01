from django.db import models

# Create your models here.


class Label(models.Model):
    title = models.CharField(max_length=50)
    prefix = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Musician(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    birthdate = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.full_name
    

class Genre(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('title',)
    
    def __str__(self):
        return self.title


class Band(models.Model):
    title = models.CharField(max_length=100)
    prefix = models.CharField(max_length=100)
    musicians = models.ManyToManyField(Musician, related_name='Music')
    website = models.URLField(blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=50)
    prefix = models.CharField(max_length=50)
    substitle = models.CharField(max_length=50)
    slug = models.URLField(unique=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    asin = models.CharField(max_length=50)
    release_date = models.DateField()
    cover_image = models.FileField(upload_to='images/')
    genre = models.ManyToManyField(Genre, related_name='Music')
    
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=50)
    song = models.FileField(upload_to='songs/')
    slug = models.SlugField(unique=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='Music')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
    
    


