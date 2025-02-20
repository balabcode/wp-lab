from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    result = None
    if request.method == 'POST':
        num1 = int(request.POST.get('num1', 0))
        num2 = int(request.POST.get('num2', 0))
        operation = request.POST.get('ops')
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'sub':
            result = num1 - num2
        elif operation == 'mul':
            result = num1 * num2
        elif operation == 'div':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
    
    return render(request, 'base.html', {'result': result})