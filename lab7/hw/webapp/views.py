from django.shortcuts import render
from .forms import GroceryForm

def index(request):
    grocery_items = [
        {'name': 'Wheat', 'price': 40},
        {'name': 'Jaggery', 'price': 50},
        {'name': 'Dal', 'price': 80},
    ]
    
    if request.method == 'POST':
        form = GroceryForm(request.POST)
        if form.is_valid():
            selected_items = [
                item for item in grocery_items 
                if form.cleaned_data.get(item['name'].lower())
            ]
            return render(request, 'index.html', {
                'form': form,
                'items': grocery_items,
                'selected_items': selected_items
            })
    else:
        form = GroceryForm()
    
    return render(request, 'index.html', {
        'form': form,
        'items': grocery_items
    })