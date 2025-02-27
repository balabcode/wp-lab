from django import forms

class GroceryForm(forms.Form):
    wheat = forms.BooleanField(required=False)
    jaggery = forms.BooleanField(required=False)
    dal = forms.BooleanField(required=False)