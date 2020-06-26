from django.urls import path

from .views import (article_list_view,
                        article_detail_view,
                        article_create_view) 

app_name='blogs'
urlpatterns = [
    path('create/',article_create_view,name='article-create'),
    path('articles/<int:id>/',article_detail_view,name='article-detail'),
    path('list/',article_list_view,name='article-list'),
]                        