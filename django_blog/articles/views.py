from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'articles/index.html',
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
