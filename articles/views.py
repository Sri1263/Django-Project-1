from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Article
from .forms import ArticleForm

# Create your views here.
def article_detail_view(request,id=None):
    obj = None
    if id is not None:
        obj = Article.objects.get(id=id)
    return render(request,'articles/detail.html',{'article_obj':obj})

def article_search_view(request):
    obj = None
    print(request.GET)
    
    # query = request.GET.get('q')  #   <input type="text" name="q"/>
    try:
        query = int(request.GET.get('q'))
    except:
        query = None
    
    if query is not None:
        obj = Article.objects.get(id=query)
    return render(request,'articles/search.html',{'article_obj':obj})

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = { 'form' : form }
    obj = Article()
    obj.title = None
    if form.is_valid() :
        #   obj = Article.objects.create(title=form.cleaned_data.get('title'),content=form.cleaned_data.get('content'))
        obj = form.save()
    context['article_obj'] = obj
    return render(request,'articles/create.html',context=context)