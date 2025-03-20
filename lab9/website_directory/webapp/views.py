from django.shortcuts import render, redirect
from .forms import CategoryForm, PageForm
from .models import Category

def index(request):
    if request.method == 'POST':
        if 'category_submit' in request.POST:
            category_form = CategoryForm(request.POST)
            if category_form.is_valid():
                category_form.save()
        else:
            page_form = PageForm(request.POST)
            if page_form.is_valid():
                page_form.save()
        return redirect('index')

    categories = Category.objects.all()
    return render(request, 'webapp/index.html', {
        'categories': categories,
        'category_form': CategoryForm(),
        'page_form': PageForm()
    })
