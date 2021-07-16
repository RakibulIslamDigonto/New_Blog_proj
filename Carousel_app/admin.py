from django.contrib import admin
from .models import Feature, Slider
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
