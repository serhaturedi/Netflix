from django.shortcuts import render
from appUser.models import Profile
from .models import *

# Create your views here.

def index(request):
    context = {}
    return render(request,'index.html', context)

def indexBrowse(request, slug, cate="Null"):
    profil = Profile.objects.filter(user = request.user).get(slug=slug)

    movieFilter=Post.objects.filter(active=True)

    if cate=="Null":
        movieFilter=Post.objects.all()
    else:
        movieFilter=Post.objects.filter(category=cate)

    context = {
        "profil": profil,
        "movieFilter":movieFilter,
    }
    return render(request,'browse-index.html', context)