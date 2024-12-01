from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=False, upload_to="media/images")
    
    

    def __str__(self):
        return self.title
    



class Comment(models.Model):
    image = models.ForeignKey(Image, related_name='comments' ,on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    



