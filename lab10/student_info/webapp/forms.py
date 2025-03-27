from django import forms

class StudentForm(forms.Form):
    student_id = forms.IntegerField(label="Student ID")
    student_name = forms.CharField(label="Student Name", max_length=100)
    course_name = forms.CharField(label="Course Name", max_length=100)
    date_of_birth = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={'type': 'date'}))