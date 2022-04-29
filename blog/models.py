from django.db import models
from django.utils.text import slugify
# Create your models here.
from django.urls import reverse


'''the blog Model'''
class Blog(models.Model):
    time_created = models.DateField()
    publisher = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    content =  models.TextField()
    slug = models.SlugField(unique=True,max_length=250)
    image = models.ImageField()
    
    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug,
            'pk': self.id
        }
        return reverse('singleblog', kwargs=kwargs)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.title

    