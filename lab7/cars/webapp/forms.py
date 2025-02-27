from django import forms

class CarForm(forms.Form):
    MANUFACTURERS = [
        ('toyota', 'Toyota'),
        ('honda', 'Honda'),
        ('ford', 'Ford'),
        ('bmw', 'BMW'),
    ]
    
    manufacturer = forms.ChoiceField(choices=MANUFACTURERS, label='Car Manufacturer')
    model = forms.CharField(max_length=100, label='Model Name')