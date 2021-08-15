from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, SlugField, TextField
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Blog_app:blog_category", args={self.slug})


class Blog(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='Published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, blank=True, null=True, on_delete=CASCADE, related_name='blogs')
    slug = models.SlugField(unique=True, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    blog_thumbnail = models.ImageField(upload_to='blog_img/')
    short_discription = models.CharField(max_length=500)
    discription = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bloger')
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()  # default manager
    new_manager = NewManager()  # custom manager

    def get_absolute_url(self):
        return reverse("Blog_app:blog", args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=300)
    body = TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return f"Comment by {self.name}"
