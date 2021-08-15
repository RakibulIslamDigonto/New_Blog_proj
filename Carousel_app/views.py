from django.shortcuts import render, get_object_or_404
from .models import Feature, Slider, Products, Category, Blogs
from django.db.models import Q, query
from django.shortcuts import redirect


def feature(request):
    features = Feature.objects.all()

    context = {
        'features': features,
    }
    return render(request, 'carousel/index.html', context)


def slider(request):
    sliders = Slider.objects.all()
    features = Feature.objects.all()[:3]

    context = {
        'features': features,
        'sliders': sliders
    }
    return render(request, 'carousel/index.html', context)


def all_products(request):
    products = Products.objects.all()

    context = {
        'products': products
    }
    return render(request, 'carousel/product.html', context)


def product_details(request, slug):
    categories = Category.objects.all()
    latest_products = Products.objects.all()[:3]
    product = Products.objects.get(slug=slug)

    context = {
        'products': latest_products,
        'product': product,
        'categories': categories,


    }
    return render(request, 'carousel/product.html', context)


def all_blogs(request):
    blogs = Blogs.objects.all()

    context = {
        'blogs': blogs
    }
    return render(request, 'carousel/blog.html', context)


def product_category(request, slug=None):
    category = None
    categories = Category.objects.all()
    products = Products.objects.all()

    # if slug:
    #     category = get_object_or_404(Category, slug=slug)
    #     products = products.filter(category=category)

    context = {
        'products': products,
        'category': category,
        'categories': categories,
    }
    return render(request, 'carousel/product.html', context)
