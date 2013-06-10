# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from blog.models import *

def index_view(request):
	posts= Post.objects.all()
 	return render_to_response('index.html',context_instance=RequestContext(request,{'posts': posts}))

def post_view(request,post):
	postTitle=post.replace("-"," ")
	try:
		postSel=Post.objects.get(title__iexact=postTitle)
		return render_to_response('post.html',context_instance=RequestContext(request,{'Post': postSel}))	
	except:
		return render_to_response('404.html')