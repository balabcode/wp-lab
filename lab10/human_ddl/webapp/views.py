from django.shortcuts import render, redirect
from .models import Human
from .forms import HumanForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    humans = Human.objects.all()
    form = HumanForm()
    return render(request, 'index.html', {'humans': humans, 'form': form})

@csrf_exempt
def update_human(request):
    if request.method == 'POST':
        form = HumanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return JsonResponse({'status': 'error'})

@csrf_exempt
def delete_human(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        Human.objects.filter(first_name=first_name).delete()
        return redirect('index')
    return JsonResponse({'status': 'error'})

@csrf_exempt
def get_human_data(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        try:
            human = Human.objects.get(first_name=first_name)
            data = {
                'last_name': human.last_name,
                'phone': human.phone,
                'address': human.address,
                'city': human.city,
            }
            return JsonResponse(data)
        except Human.DoesNotExist:
            return JsonResponse({})
    return JsonResponse({'status': 'error'})