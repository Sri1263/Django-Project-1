from django import forms

# class ArticleForm(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField()

#     # def clean_title(self):
#     #     cleaned_data = self.cleaned_data
#     #     title = cleaned_data.get('title')
#     #     if title.lower().strip() == 'asd':
#     #         raise forms.ValidationError('title can\'t be asd')
#     #     return title
    
#     def clean(self):
#         if self.cleaned_data.get('title').lower().strip() == 'asd' :
#             self.add_error('title','add_error : title can\'t be asd')                       # add_error is a field Error
#             raise forms.ValidationError('ValidationError : title can\'t be asd')              # ValidationError is a non-field Error
#         return self.cleaned_data

from .models import Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']
    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        if Article.objects.filter(title__icontains=title).exists()  :
            self.add_error('title',f'\"{title}\" has already been taken')
        return data