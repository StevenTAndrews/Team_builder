from django.shortcuts import render

from projects import models

def home(request):
    projects = models.Project.objects.all()
    return render(request, 'index.html', {'projects': projects})