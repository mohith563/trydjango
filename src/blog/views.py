from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ArticleForm
# Create your views here.

def article_list_view(request):
    objects = Article.objects.all()
    context = {
        'obj_list':objects
    }
    return render(request,'blogs/article_list.html',context)

def article_detail_view(request, id):
    obj = get_object_or_404(Article, id=id)
    context = {
        'object':obj
    }
    return render(request,'blogs/article_detail.html',context)

def article_create_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleForm()
    context = {
        'form':form
    }
    return render(request,'blogs/article_create.html',context)
