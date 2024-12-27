from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    published_date = models.DateField(auto_now_add=True) 

    def __str__(self):
        return self.title
