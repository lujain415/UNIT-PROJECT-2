from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Entry

# Create your views here.

def entry_search(request):
    if 'search' in request.GET:
        query = request.GET['search']
        results = Entry.objects.filter(title__icontains=query)
    else:
        results = Entry.objects.none()

    return render(request, 'main/entry_search.html', {'results': results})