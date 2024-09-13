from django.shortcuts import render
from .models import NewsPost
from django.http import HttpResponse

def index(request):
    news_posts = NewsPost.objects.all()
    return render(request, 'index.html', {'x': news_posts})
