"""Django_Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home),

    url(r'^(?P<cat_id>[0-9]+)/showCatPosts/$',views.showCatPosts),
    
    

    url(r'^post/(?P<post_id>[0-9]+)$', views.getPost),
    url(r'^comment/(?P<comment_id>[0-9]+)/(?P<post_id>[0-9]+)$', views.reply),
    url(r'^post/addLike/(?P<post_id>[0-9]+)$', views.addLike),  
    url(r'^post/DisLike/(?P<post_id>[0-9]+)$', views.DisLike), 

    
]
