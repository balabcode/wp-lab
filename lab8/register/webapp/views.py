from django.shortcuts import render
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            contact_number = form.cleaned_data['contact_number']
            return render(request, 'webapp/success.html', {
                'username': username,
                'email': email,
                'contact_number': contact_number,
            })
    else:
        form = RegisterForm()
    return render(request, 'webapp/register.html', {'form': form})

def success(request):
    return render(request, 'webapp/success.html')
