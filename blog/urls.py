from django.urls import path

from blog.views import index, ola ,post_show, PostDetailView# Nesta linha importamos as function views.

urlpatterns = [
    path('index/', index, name= "index"), # Definir a rota /index
    path('ola/', ola, name="ola"), # Definir a rota /ola
    path('posts/all', ola, name="posts_list"),
    path('post/<int:post_id>', post_show, name="exibe_post"),
    path('post/<int:pk>/show', PostDetailView.as_view(), name="post_detail"),

]