from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'video', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'content': forms.Textarea(attrs={'class': 'form-control custom-input', 'rows': 4}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control custom-input'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control custom-input'}),
        }
