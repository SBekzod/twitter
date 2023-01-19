from django.http import HttpResponse
from django.shortcuts import render
from .models import Tweet

# Create your views here.
def home_view(request, *arg, **kwargs):
  print(kwargs)
  return HttpResponse("<h1>Hello World!!!</h1>")

def tweet_check(request, tweet_id, *args, **kwargs):
  print(request.GET['nick']) 
  print('args:', args)
  print('kwarngs:', kwargs)
  return HttpResponse(f"<div>Tweet on param: <strong>{tweet_id}</strong> and query <strong>{request.GET['nick']}</strong></div>")

def tweet_detail_view(request, *args, **kwargs):
  print('kwarngs:', kwargs)
  obj = Tweet.objects.get(id=kwargs['tweet_id'])
  return HttpResponse(f"<div>Tweet details: No <strong>{kwargs['tweet_id']}</strong> and content <strong>{obj.content}</strong></div>")


