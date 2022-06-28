from django.shortcuts import render
from Blog.models import Post
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):
    posts = Post.objects.all().reverse()
    variaveis = {
        'posts':posts,
    }
    #posts = Post.objects.all()#Retorana todos os posts criados no site de Administração Django
    return render(request,'Index.html',variaveis)

def post(request,my_id):
    post = Post.objects.get(id=my_id)
    post2 = get_object_or_404(Post, pk=my_id)
    contador = list()
    for i in range(1,10):
        contador.append(i)
    
    variaveis = {
        'post':post,
        'contador':contador,
    }
    return render(request,'Post.html',variaveis)


