from django.shortcuts import render, redirect
from .forms import StudentForm

def first_page(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            request.session['student_data'] = form.cleaned_data
            return redirect('second_page')
    else:
        form = StudentForm()
    return render(request, 'webapp/firstpage.html', {'form': form})

def second_page(request):
    student_data = request.session.get('student_data', {})
    display_text = f"Name: {student_data.get('name', '')}, Roll: {student_data.get('roll', '')}, Subject: {student_data.get('subject', '')}"
    if request.method == 'POST':
        return redirect('first_page')
    return render(request, 'webapp/secondpage.html', {'display_text': display_text})