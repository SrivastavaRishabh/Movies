from django.db import models

# Create your models here.


class PersonType(models.Model):
    """Person type model."""
    title = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.title
    

class Person(models.Model):
    """Person model."""
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField()
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, blank=True, null=True)
    image = models.FileField(upload_to=('images/'), blank=True)
    birth_date = models.DateField()
    person_types = models.ManyToManyField(PersonType)
    website = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name
    
