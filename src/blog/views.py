from django.shortcuts import render, get_object_or_404

# Create your views here.

def article_list_view(request):
    return render(request,'blogs/article_list.html',{})
