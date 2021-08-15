from django.urls import path
from .import views

app_name = 'Carousel_app'

urlpatterns = [
    #path('', views.feature, name='feature'),
    path('', views.slider, name='slider'),
    #path('<slug:product_category>', views.product_category, name='product_category'),
    path('products/', views.all_products, name='all_products'),
    path('blogs/', views.all_blogs, name='all_blogs'),
    #path('product/', views.product, name='product'),
]
