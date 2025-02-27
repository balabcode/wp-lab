from django.shortcuts import render
from .forms import CarForm

def car_view(request):
    result = None
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            result = {
                'manufacturer': form.cleaned_data['manufacturer'],
                'model': form.cleaned_data['model']
            }
    else:
        form = CarForm()
    
    return render(request, 'index.html', {
        'form': form,
        'result': result
    })