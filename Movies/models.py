from django.db import models
from django.template.defaultfilters import slugify

gender = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    birth_date = models.DateField()
    website = models.URLField(max_length=200)
    email_id = models.EmailField()
    gender = models.CharField(
        choices=gender,
        default='male',
        max_length=6
    )

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Studio(models.Model):
    title = models.CharField(max_length=100)
    prefix = models.CharField(max_length=50)
    website = models.URLField(max_length=200)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Studio, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=200)
    prefix = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    directors = models.ManyToManyField("Director",
                                       related_name='moviedirector')
    studio = models.ForeignKey("Studio",
                               on_delete=models.CASCADE,
                               related_name='moviestudio')
    release_date = models.DateField()
    cover_image = models.FileField(upload_to=('images/'))
    review = models.TextField()
    genre = models.ManyToManyField("Genre", related_name='moviegenre')
    asin = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
