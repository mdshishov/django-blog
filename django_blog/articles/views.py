from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.urls import reverse

from .models import Article
from .forms import ArticleForm


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


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(
            request,
            'articles/create.html',
            context={
                'form': form,
            }
        )

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles_index')

        return render(
            request,
            'articles/create.html',
            context={
                'form': form,
            }
        )
