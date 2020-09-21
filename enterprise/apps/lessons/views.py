from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html',{'latest_articles_list': latest_articles_list})