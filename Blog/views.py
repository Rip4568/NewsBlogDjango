from django.shortcuts import render
from django.http import HttpResponse
from Blog.models import Post
# Create your views here.

def home(request):
    posts = Post.objects.all()
    variaveis = {
        'posts':posts,
    }
    #posts = Post.objects.all()#Retorana todos os posts criados no site de Administração Django
    return render(request,'index.html',variaveis)

def post(request,my_id):
    post = Post.objects.get(id=my_id)
    variaveis = {
        'post':post
    }
    return render(request,'static/Post.html',variaveis)


