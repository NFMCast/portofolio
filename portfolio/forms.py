from django.forms import ModelForm
from django import forms

from portfolio.models import BlogPost

class BlogPostForm(ModelForm):
    descricao = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))

    class Meta:
        model = BlogPost
        fields = '__all__'
