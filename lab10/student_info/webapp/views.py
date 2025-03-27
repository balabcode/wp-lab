from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def index(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            student_name = form.cleaned_data['student_name']
            course_name = form.cleaned_data['course_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            Student.objects.create(
                student_id=student_id,
                student_name=student_name,
                course_name=course_name,
                date_of_birth=date_of_birth,
            )
            return redirect('index')
    else:
        form = StudentForm()
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students, 'form': form})