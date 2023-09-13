import json

from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt


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

def get_all_posts(request):
    posts = list(Post.objects.values('pk', 'body_text', 'pub_date'))
    data = {'success': True, 'posts': posts}
    json_data = json.dumps(data, indent=1, cls=DjangoJSONEncoder)
    response = HttpResponse(json_data, content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*' # requisição de qualquer origem
    return response

def get_post(request, post_id):
    post = Post.objects.filter(
        pk=post_id
        ).values(
        'pk', 'body_text', 'pub_date'
        ).first()
    data = {'success': True, 'post': post}
    status = 200
    if post is None:
        data = {'success': False, 'error': 'Post ID não existe.'}
        status=404
    response = HttpResponse(
        json.dumps(data, indent=1, cls=DjangoJSONEncoder),
        content_type="application/json",
        status=status
    )
    response['Access-Control-Allow-Origin'] = '*' # requisição de qualquer origem
    return response

class PostCreateView(CreateView):
    model = Post
    template_name = 'post/post_form.html'
    fields = ('body_text', )
    success_url = reverse_lazy('posts_list')

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        body_text = data.get('body_text')
        if body_text is None:
            data = {'success': False, 'error': 'Texto do post inválido.'}
            status = 400 # Bad Request => erro do client
        else:
            post = Post(body_text=body_text)
            post.save()
            post_data = Post.objects.filter(
                pk=post.id
             ).values(
                 'pk', 'body_text', 'pub_date'
                 ).first()
            data = {'success': True, 'post': post_data}
            status = 201 # Created

    response = HttpResponse(
        json.dumps(data, indent=1, cls=DjangoJSONEncoder),
        content_type="application/json",
        status=status
)
    response['Access-Control-Allow-Origin'] = '*'

    return response
  

    
    

