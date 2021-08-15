from django.contrib import admin
from .models import Feature, Slider, Products, Category
# Register your models here.


class FeatureAdmin(admin.ModelAdmin):

    list_display = [
        'heading',
        'slug',
        'thumbnail',
        'short_discription',
        'discription'
    ]


admin.site.register(Feature, FeatureAdmin)


class SliderAdmin(admin.ModelAdmin):

    list_display = [
        'heading',
        'thumbnail',
        'short_discription'
    ]


admin.site.register(Slider, SliderAdmin)


class ProductsAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'thumbnail',
        'short_discription'
    ]


admin.site.register(Products, ProductsAdmin)


class CategoryAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'slug'
    ]

admin.site.register(Category, CategoryAdmin)
