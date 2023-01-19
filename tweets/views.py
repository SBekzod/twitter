from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *arg, **kwargs):
  print(kwargs)
  return HttpResponse("<h1>Hello World!!!</h1>")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
  print(request.GET['nick']) 
  print('args:', args)
  print('kwarngs:', kwargs)
  return HttpResponse(f"<div>Tweet on param: <strong>{tweet_id}</strong> and query <strong>{request.GET['nick']}</strong></div>")

