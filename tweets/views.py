from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import Tweet

# Create your views here.
def home_view(request, *arg, **kwargs):
  print(kwargs)
  return render(request, 'pages/home.html', context={"name": "martin"}, status=200) 

def tweet_detail_api(request, tweet_id, *args, **kwargs):
  """
  Organize Rest API 
  """
  data = {"id": tweet_id}
  try:
    obj = Tweet.objects.get(id=tweet_id)
    data['content'] = obj.content
    status = 200
  except:
    data['message'] = 'tweet with that id is not found!'
    status = 404
  return JsonResponse(data, status=status)



def tweet_check(request, tweet_id, *args, **kwargs): 
  print(request.GET['nick'])  
  print('kwarngs:', kwargs)
  return HttpResponse(f"<div>Tweet on param: <strong>{tweet_id}</strong> and query <strong>{request.GET['nick']}</strong></div>")

def tweet_detail_view(request, *args, **kwargs):
  try:
    print('kwarngs:', kwargs)
    obj = Tweet.objects.get(id=kwargs['tweet_id']) 
  except:
    raise Http404
  return HttpResponse(f"<div>Tweet details: No <strong>{kwargs['tweet_id']}</strong> and content <strong>{obj.content}</strong></div>")

    
