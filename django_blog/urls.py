"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from blog.views import *
from django.conf.urls.static import static
from django.conf import settings
import DjangoUeditor
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^$', ArticleView.as_view(), name='index'),
    url(r'^article/(?P<title>.*)$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^category/(?P<category>\S+)$', CategoryListView.as_view(), name='category'),
    url(r'^tag/(?P<tag>\S+)$', TagListView.as_view(), name='tag'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^archive/$', ArchiveView.as_view(), name='archive'),
    url(r'^message/$', MessageView.as_view(), name='message'),
    url(r'^me/$', Me.as_view(), name='me'),
]

urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
