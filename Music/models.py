from django.db import models
from django.template.defaultfilters import slugify


class Label(models.Model):
    title = models.CharField(max_length=50)
    prefix = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Label, self).save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Band(models.Model):
    title = models.CharField(max_length=100)
    prefix = models.CharField(max_length=100)
    musicians = models.ManyToManyField(Musician, related_name='band_musicians')
    website = models.URLField(blank=True)
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Band, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=100)
    prefix = models.CharField(max_length=50)
    substitle = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='album_band')
    label = models.ForeignKey(Label, on_delete=models.CASCADE, related_name='album_label')
    asin = models.CharField(max_length=50)
    release_date = models.DateField()
    cover_image = models.FileField(upload_to='images/')
    genre = models.ManyToManyField(Genre, related_name='album_genre')
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Album, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=50)
    song = models.FileField(upload_to='songs/')
    slug = models.SlugField(unique=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='track_album')
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Track, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
