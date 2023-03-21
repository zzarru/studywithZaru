from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


# def new(request):
#     return render(request, 'articles/new.html')


def create(request):
    if request.method == 'POST':
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        form = ArticleForm(request.POST)
        if form.is_valid(): #유효성 검사 후에 
            article = form.save()
            return redirect('articles:detail', article.pk)        
        # return redirect('articles:create')
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'articles/create.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {'article': article}
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)        
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.save()
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {'form': form, 'article': article}
        
    return render(request, 'articles/update.html', context)