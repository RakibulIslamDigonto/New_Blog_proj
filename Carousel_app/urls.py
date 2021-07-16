from django.urls import path
from .import views

app_name = 'Carousel_app'

urlpatterns = [
    #path('', views.feature, name='feature'),
    path('', views.slider, name='slider')
]
