from django import forms

class MagazineCoverForm(forms.Form):
    title = forms.CharField(max_length=100)
    subtitle = forms.CharField(max_length=100)
    image = forms.ImageField()
    background_color = forms.CharField(max_length=7, initial="#FFFFFF")
    font_color = forms.CharField(max_length=7, initial="#000000")
    font_size = forms.IntegerField(initial=30)
