from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from .models import Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(
            request,
            'articles/index.html',
            context={
                'articles': articles,
            },
        )


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            'articles/detail.html',
            context={
                'article': article,
            }
        )


def index(request, tag, article_id):
    return render(
        request,
        'articles/index.html',
        context={
            'tag': tag,
            'article_id': article_id,
        }
    )


def index_redirect(request):
    return redirect(
        reverse(
            'articles:article_page',
            kwargs={'tag': 'python', 'article_id': 42}
        )
    )
