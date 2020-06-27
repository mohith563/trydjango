from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Article
from .forms import ArticleModelForm
# Create your views here.

from django.views.generic import (CreateView,
                                ListView,
                                DetailView,
                                DeleteView,
                                UpdateView)


class ArticleListView(ListView):
    template_name = 'blog/article_list.html' #<blog>/<modelname>_list.html
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html' #<blog>/<modelname>_list.html
    queryset = Article.objects.all() #Not necessary but it can be used to filter the queryset
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleModelForm
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_update.html'
    form_class = ArticleModelForm
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html' #<blog>/<modelname>_list.html
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)
    def get_success_url(self):
        return reverse('articles:article-list')

# def article_list_view(request):
#     objects = Article.objects.all()
#     context = {
#         'obj_list':objects
#     }
#     return render(request,'blogs/article_list.html',context)

# def article_detail_view(request, id):
#     obj = get_object_or_404(Article, id=id)
#     context = {
#         'object':obj
#     }
#     return render(request,'blogs/article_detail.html',context)

# def article_create_view(request):
#     form = ArticleForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ArticleForm()
#     context = {
#         'form':form
#     }
#     return render(request,'blogs/article_create.html',context)
