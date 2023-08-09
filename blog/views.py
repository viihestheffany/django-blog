from django.shortcuts import render

# incluir a class Httresponse.
from django.http import HttpResponse

# Definir uma function view chamada index.
def index(request):
    #return HttpResponse('olá django - index')
    #return render(request, 'index.html')
    return render(request, 'index.html', {'titulo': 'Últimos Artigos'})

def ola(request):
    # return HttpResponse('ola Django')
    return render(request, 'home.html')