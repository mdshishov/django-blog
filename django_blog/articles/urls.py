from django.urls import path
from django_blog.articles import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='articles'),
    path('<str:tag>/<int:article_id>/', views.index, name='article_page'),
    path('<int:id>', views.ArticleView.as_view(), name='articles_detail')
]