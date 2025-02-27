from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    roll = forms.CharField(max_length=10)
    subject = forms.ChoiceField(choices=[
        ('math', 'Mathematics'),
        ('sci', 'Science'),
        ('eng', 'English')
    ])