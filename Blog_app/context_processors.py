
from .models import Blog, Category


def recent_post(request):
    blogs = Blog.objects.all().order_by('-id')[:4]

    return {
        'blogs': blogs

    }


def all_category(request):
    categories = Category.objects.all()

    return {
        'categories': categories

    }
