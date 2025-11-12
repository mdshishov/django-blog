from django.urls import path
from django_blog.articles import views

app_name = 'articles'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:tag>/<int:article_id>/', views.index, name='article_page'),
]