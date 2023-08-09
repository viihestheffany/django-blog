from django.shortcuts import render
from blog.models import Post

# incluir a class Httresponse.
from django.http import HttpResponse

# Definir uma function view chamada index.
def index(request):
    #return HttpResponse('olá django - index')
    #return render(request, 'index.html')
    return render(request, 'index.html', {'titulo': 'Últimos Artigos'})

#def ola(request):
    # return HttpResponse('ola Django')
    return render(request, 'home.html')

def ola(request): 
    posts = Post.objects.all() 
    context = {'posts_list': posts }
    return render(request, 'posts.html', context)