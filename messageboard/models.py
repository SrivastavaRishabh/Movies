from django.db import models

# Create your models here.
class message(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True , null=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    
