from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from . import models
from . import forms

@login_required
def project_detail(request, pk):
    '''Show project detail'''
    project = get_object_or_404(models.Project, pk=pk)
    positions = models.Position.objects.filter(project_id=pk)
    return render(request, 'projects/project.html', {
        'project': project,
        'positions': positions })


@login_required
def create_project(request):
    '''Create a new project and positions'''
    form = forms.ProjectForm()
    position_formset = forms.PositionInlineFormSet(
        queryset=models.Position.objects.none()
    )

    if request.method == 'POST':
        form = forms.ProjectForm(request.POST)
        position_formset = forms.PositionInlineFormSet(
            request.POST,
            queryset=models.Position.objects.none()
        )

        if form.is_valid() and position_formset.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            position_instance = position_formset.save(commit=False)
            for obj in position_formset.deleted_objects:
                obj.delete()
            for position in position_instance:
                position.project = project
                position.save()
            return HttpResponseRedirect(reverse('home'))

    return render(request, 'projects/project_new.html', {
        'form': form,
        'position_formset': position_formset
        })


@login_required
def edit_project(request, pk):
    '''Update the project and positions'''
    try:
        project = models.Project.objects.get(pk=pk, user=request.user)
    except ObjectDoesNotExist:
        project = None

    form = forms.ProjectForm(instance=project)
    position_formset = forms.PositionInlineFormSet(
        queryset=models.Position.objects.filter(
            project_id=pk,
            project__user=request.user)
    )

    if request.method == 'POST':
        form = forms.ProjectForm(request.POST, instance=project)
        position_formset = forms.PositionInlineFormSet(
            request.POST,
            queryset=models.Position.objects.filter(
                project_id=pk,
                project__user=request.user)
        )

        if form.is_valid() and position_formset.is_valid():
            form.save()
            position_instance = position_formset.save(commit=False)
            for position in position_instance:
                position.project = project
                position.save()
            for position in position_formset.deleted_objects:
                position.delete()
            return HttpResponseRedirect(reverse("home"))

    return render(request, 'projects/project_edit.html', {
                'form': form,
                'position_formset': position_formset
            })