from django import forms
from .models import Category, Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['category', 'title', 'url', 'views']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'visits', 'likes']
