from django.urls import path
from .import views
from django.urls import reverse

app_name = 'Blog_app'

urlpatterns = [
    # path('', views.home_blog, name='home_blog'),
    path('', views.all_blog, name='all_blog'),
    path('<slug:blog>/', views.blog, name='blog'),
    path('all/categories/', views.all_blog_category, name='all_blog_category'),

    path('category/<slug:slug_of_category>/',
         views.blog_category, name='blog_category'),

    path('about/us/', views.about, name='about'),
    path('search/blog/', views.search_blog, name='search_blog'),
]
