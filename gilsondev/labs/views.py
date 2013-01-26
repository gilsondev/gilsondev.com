# -*- coding: utf8 -*-

from django.shortcuts import render

from gilsondev.labs.models import Project


def list(request):
    projects = Project.objects.all()
    return render(request, 'labs/project_list.html', {
        'projects': projects,
    })
