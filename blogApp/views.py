from django.shortcuts import render

from blogApp.models import Blog


def home_page(request):
    context = {
        'name': 'Saurav Adhikari'
    }
    return render(request, 'index.html', context)


def blog_page(request):
    obj = Blog.objects.all()
    context = {
        'object' : obj
    }
    return render(request, 'blog.html', context)
