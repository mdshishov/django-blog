from django.urls import path
from django_blog.article import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
]