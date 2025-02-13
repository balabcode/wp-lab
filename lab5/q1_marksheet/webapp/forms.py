from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100, label='Student Name')
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Date of Birth')
    address = forms.CharField(widget=forms.Textarea, label='Address')
    contact_number = forms.CharField(max_length=15, label='Contact Number')
    email = forms.EmailField(label='Email ID')
    english_marks = forms.IntegerField(min_value=0, max_value=100, label='Marks in English')
    physics_marks = forms.IntegerField(min_value=0, max_value=100, label='Marks in Physics')
    chemistry_marks = forms.IntegerField(min_value=0, max_value=100, label='Marks in Chemistry')