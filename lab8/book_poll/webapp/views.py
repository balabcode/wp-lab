from django.shortcuts import render, redirect
from .models import Vote
from .forms import VoteForm
from django.db.models import Count

def index(request):
    show_results = False
    percentages = {}
    total_votes = 0
    
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/?results=1')
    else:
        form = VoteForm()
        if request.GET.get('results'):
            show_results = True
            total_votes = Vote.objects.count()
            results = Vote.objects.values('choice').annotate(count=Count('choice'))
            percentages = {result['choice']: round((result['count'] / total_votes) * 100, 2) 
                         if total_votes else 0 for result in results}

    return render(request, 'webapp/index.html', {
        'form': form,
        'show_results': show_results,
        'percentages': percentages,
        'total_votes': total_votes
    })
