from django.shortcuts import render
from .forms import EmployeePromotionForm
from datetime import datetime

# Create your views here.

def employee_form(request):
    current_date = datetime.today()
    date_format = r"%d/%m/%Y"

    employee_data = None
    promoted = None

    if request.method == 'POST':
        form = EmployeePromotionForm(request.POST)
        if form.is_valid():
            join_date_string = form.cleaned_data['doj']
            join_date = datetime.strptime(join_date_string, date_format)
            time_elapsed = current_date - join_date
            if (time_elapsed.days / 365.25) > 5:
                promoted = True
            else:
                promoted = False
            
            employee_data = {
                'doj': join_date_string,
                'promoted': promoted,
            }
    else:
        form = EmployeePromotionForm()

    return render(
        request,
        'webapp/employee_form.html',
        {
            'form': form,
            'employee_data': employee_data,
            'promoted': "YES" if promoted else "NO" if promoted is not None else "N/A"
        }
    )
