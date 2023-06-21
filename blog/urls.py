from django.urls import path

from blog.views import index, ola # Nesta linha importamos as function views.

urlpatterns = [
    path('index/', index, name= "index"), # Definir a rota /index
    path('ola/', ola, name="ola") # Definir a rota /ola
]