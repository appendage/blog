#coding:utf-8
from django.conf.urls import include, url
from django.contrib import admin
from blog.views import *
from django.conf.urls.static import static
from django.conf import settings
from DjangoUeditor import urls as DjangoUeditor_urls
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor/',include(DjangoUeditor_urls)),
    url(r'^$', ArticleView.as_view(), name='index'),
    url(r'^article/(?P<title>.*)$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^category/(?P<category>\S+)$', CategoryListView.as_view(), name='category'),
    url(r'^tag/(?P<tag>\S+)$', TagListView.as_view(), name='tag'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^archive/$', ArchiveView.as_view(), name='archive'),
    url(r'^message/$', MessageView.as_view(), name='message'),
    url(r'^me/$', Me.as_view(), name='me'),
]
