from django.shortcuts import render
from .forms import WorksForm, CompanySearchForm
from .models import Works, Lives
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        # Handle Works form submission
        if 'submit_works' in request.POST:
            works_form = WorksForm(request.POST)
            if works_form.is_valid():
                works_form.save()
                messages.success(request, 'Data inserted successfully!')
        
        # Handle company search
        elif 'submit_search' in request.POST:
            search_form = CompanySearchForm(request.POST)
            if search_form.is_valid():
                company = search_form.cleaned_data['company_name']
                employees = Works.objects.filter(company_name=company)
                results = []
                for emp in employees:
                    try:
                        lives = Lives.objects.get(person_name=emp.person_name)
                        city = lives.city
                    except Lives.DoesNotExist:
                        city = 'Unknown'
                    results.append({
                        'name': emp.person_name,
                        'company': emp.company_name,
                        'salary': emp.salary,
                        'city': city
                    })
                return render(request, 'webapp/index.html', {
                    'works_form': WorksForm(),
                    'search_form': CompanySearchForm(),
                    'results': results,
                    'searched_company': company
                })
    
    return render(request, 'webapp/index.html', {
        'works_form': WorksForm(),
        'search_form': CompanySearchForm()
    })
