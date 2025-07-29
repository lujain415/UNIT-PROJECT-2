from django.shortcuts import render,get_object_or_404,redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.


def article_list(request):
    articles = Article.objects.order_by('-created_at')
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:article_list')  
    else:
        form = ArticleForm()
    return render(request, 'blog/article_form.html', {'form': form})


def article_update(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('blog:article_detail', article_id=article.id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/article_form.html', {'form': form, 'update': True})

def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('blog:article_list')
    return render(request, 'blog/article_confirm_delete.html', {'article': article})