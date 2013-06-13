# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from blog.models import *


def index_view(request):
    posts = Post.objects.all()
    return render_to_response('index.html', context_instance=RequestContext(request, {'posts': posts}))
