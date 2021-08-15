from django.db import models
from django.db.models.fields import SlugField
from django.urls import reverse


# Create your models here.
class Feature(models.Model):
    heading = models.CharField(max_length=100)
    slug = models.SlugField()
    thumbnail = models.ImageField(upload_to='carousel/images/')
    short_discription = models.TextField()
    discription = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        return reverse('Carousel_app:porduct', kwargs={'slug': self.slug})


class Slider(models.Model):
    heading = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='slider_image/')
    short_discription = models.TextField()

    def __str__(self):
        return self.heading


class Products(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='product_image/')
    short_discription = models.TextField()
    category = models.ForeignKey(
        'Category', blank=True, null=True, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Carousel_app:blog_details', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        return reverse('Carousel_app.views.products', args=[self.slug])

# class Category(models.Model):
#     products = models.ForeignKey(Products, blank=True, null=True, related_name='category', on_delete=models.CASCADE)
#     category_name = models.CharField(max_length=200)
#     slug = models.SlugField(unique=True)


#     class Meta:
#         unique_together = ('slug', 'products',)
#         verbose_name_plural = "categories"

#     def __str__(self):
#         return self.category_name


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    blog_thumbnail = models.ImageField(upload_to='blogs_image/')
    discription = models.TextField()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=170)
    slug = models.SlugField(max_length=170, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Carousel_app:product_category', args={self.slug})
