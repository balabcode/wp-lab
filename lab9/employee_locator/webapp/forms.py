from django import forms
from .models import Works

class WorksForm(forms.ModelForm):
    class Meta:
        model = Works
        fields = '__all__'
        widgets = {
            'person_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CompanySearchForm(forms.Form):
    company_name = forms.CharField(
        label='Search by Company',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
