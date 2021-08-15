from django.contrib import admin
from .models import Blog, Comment, Category
# Register your models here.


class BlogAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'slug',
        'blog_thumbnail',
        'short_discription',
        'discription',
        'publish',
        'creation'
    ]


admin.site.register(Blog, BlogAdmin)


class CommentAdmin(admin.ModelAdmin):

    list_display = [
        'blog',
        'name',
        'body',
        'publish',
        'status',
    ]


admin.site.register(Comment, CommentAdmin)

class CategoryAdmin(admin.ModelAdmin):

    list_display = [
        'name',

    ]


admin.site.register(Category, CategoryAdmin)