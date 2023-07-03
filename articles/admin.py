from django.contrib import admin

from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    search_fields = ['title','id']

admin.site.register(Article,ArticleAdmin)