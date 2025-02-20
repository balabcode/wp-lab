from django.shortcuts import render
from .forms import MagazineCoverForm

def create_cover(request):
    if request.method == 'POST':
        form = MagazineCoverForm(request.POST, request.FILES)
        if form.is_valid():
            return render(request, 'webapp/show_cover.html', {'form': form})
    else:
        form = MagazineCoverForm()
    return render(request, 'webapp/create_cover.html', {'form': form})
