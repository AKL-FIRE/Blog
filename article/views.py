from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from article.models import Article
from django.http import Http404
# Create your views here.
def home(request):
    post_list = Article.objects.all() #获取所有Article对象
    return render(request, 'home.html', {'post_list':post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post':post})

def about_me(request):
    return render(request, 'aboutme.html')

def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list':post_list, 'error':False})

def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact=tag)  # contains
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})

def search_date(request, date):
    try:
        post_list = Article.objects.filter(date_time__date=date)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'date.html', {'post_list':post_list})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : True})
            else :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : False})
    return redirect('/')