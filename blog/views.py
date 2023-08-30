from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
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

def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/detail.html', {'post': post})

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'
