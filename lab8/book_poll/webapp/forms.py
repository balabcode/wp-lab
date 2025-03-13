from django import forms
from .models import Vote

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['choice']
        widgets = {
            'choice': forms.RadioSelect(attrs={'class': 'form-check-input'})
        }
