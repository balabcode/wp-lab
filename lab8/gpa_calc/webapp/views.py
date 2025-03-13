from django.shortcuts import render, redirect
from .forms import StudentForm

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            request.session['name'] = form.cleaned_data['name']
            request.session['cgpa'] = form.cleaned_data['total_marks'] / 50
            return redirect('result')
    else:
        form = StudentForm()
    return render(request, 'webapp/home.html', {'form': form})

def result(request):
    if 'name' not in request.session or 'cgpa' not in request.session:
        return redirect('home')
    return render(request, 'webapp/result.html')
