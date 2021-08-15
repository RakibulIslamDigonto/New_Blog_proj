from .forms import CommentForm
from django.conf.urls import url
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Blog, Category
from django.shortcuts import redirect
from django.views.generic import View
from django.urls import reverse
from django.http import Http404
from django.db.models import Q

# Create your views here.


def blog_category(request, slug_of_category):
    category = get_object_or_404(Category, slug=slug_of_category)
    blogs = Blog.objects.filter(category=category)

    # paginator = Paginator(category, 2)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    context = {
         'blogs': blogs,
        # 'page_obj_category': page_obj,
    }
    return render(request, 'blog_temp/category.html', context)


def all_blog_category(request):
    all_categories = Category.objects.all()
    context = {
        'all_categories': all_categories
    }

    return render(request, 'blog_temp/all_category.html', context)


def all_blog(request):
    all_blogs = Blog.objects.all()
    #all_blogs = Blog.new_manager.all()
    paginator = Paginator(all_blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'all_blogs': all_blogs,
        'page_obj': page_obj

    }

    return render(request, 'blog_temp/index.html', context)


# def home_blog(request):
#     home_blogs = Blog.objects.all()
#     #all_blogs = Blog.new_manager.all()
#     paginator = Paginator(home_blogs, 4)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     context = {
#         'home_blogs': home_blogs,
#         'all_page_obj': page_obj

#     }

#     return render(request, 'blog_temp/home_page.html', context)


def blog(request, blog):
    s_blog = get_object_or_404(Blog, slug=blog, status='published')
    comments = s_blog.comment.filter(status=True)

    user_comments = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            user_comments = comment_form.save(commit=False)
            user_comments.blog = s_blog
            user_comments.save()
            return HttpResponseRedirect('/' + s_blog.slug)
    else:
        comment_form = CommentForm()

    context = {
        'single_blog': s_blog,
        'comments': comments,
        'user_comments': user_comments,
        'comment_form': comment_form
    }
    return render(request, 'blog_temp/single_blog.html', context)


def search_blog(request):
    latest_blog = Blog.objects.all()[:3]
    #queryset = Blog.objects.all()
    query = request.GET.get('q')

    if query:
        queryset = (
            Q(title__icontains=query) | Q(short_discription__icontains=query) | Q(
                discription__icontains=query)
        )
        result = Blog.objects.filter(queryset)

    context = {
        # 'queryset': queryset,
        'latest_blog': latest_blog,
        'result': result,
        'query': query
    }

    return render(request, 'blog_temp/search.html', context)


def about(request):
    paginator = Paginator()
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'blog_temp/about.html')
