from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article

def home_view(request):
    objs = Article.objects.all()
    string = render_to_string('home_view.html',{'obj_list':objs})
    return HttpResponse(string)