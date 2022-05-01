from cloudinary.models import CloudinaryField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
'''the blog Model'''
class Blog(models.Model):
    time_created = models.DateField(auto_now=True)
    publisher = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    content =  models.TextField()
    slug = models.SlugField(unique=True,max_length=250)
    image = CloudinaryField('image')
    
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

    def save_blog(self):
        self.save()

    def delete_blog(self):
        self.delete()
    
    @classmethod
    def search_blog(cls, title):
        blog = Blog.objects.filter(title__icontains = title)
        return blog

    def update_blog(self, *args, **kwargs):
        return type(self).objects.filter(pk=self.pk).update(*args, **kwargs)
