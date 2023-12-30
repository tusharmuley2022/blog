# forms.py
from django import forms
from .models import Article

class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body']  # Add more fields as needed

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body']