"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from article import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('article/<id>', views.detail, name='detail'),
    path('aboutme/', views.about_me, name='aboutme'),
    path('archives/', views.archives, name='archives'),
    path('tag/<tag>', views.search_tag, name = 'search_tag'),
    path('date/<date>', views.search_date, name='search_date'),
    path('search/', views.blog_search, name='search'),
]
