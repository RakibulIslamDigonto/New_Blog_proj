from django.db import models


# Create your models here.
class Feature(models.Model):
    heading = models.CharField(max_length=100)
    slug = models.SlugField()
    thumbnail = models.ImageField(upload_to = 'carousel/images/')
    short_discription = models.TextField()
    discription = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading




class Slider(models.Model):
    heading = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to = 'slider_image/')
    short_discription = models.TextField()

    def __str__(self):
        return self.heading