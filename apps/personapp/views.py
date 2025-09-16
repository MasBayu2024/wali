from django.shortcuts import render
from .models import Person

def home(request):
    # optionally pass some stats
    person_count = Person.objects.count() if Person.objects.exists() else 0
    return render(request, 'home.html', {'person_count': person_count})

def person_list(request):
    # optionally add ordering or pagination
    persons = Person.objects.all().order_by('id')
    return render(request, 'person_list.html', {'persons': persons})
