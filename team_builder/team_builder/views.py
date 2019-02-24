from django.shortcuts import render

from projects import models

def home(request):
    projects = models.Project.objects.all()
    return render(request, 'index.html', {'projects': projects})


def search_term(request):
    term = request.GET.get('q')
    projects = models.Project.objects.filter(name__icontains=term)
    return render(request, 'index.html', {'projects': projects})