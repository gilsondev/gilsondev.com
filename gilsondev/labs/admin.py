# -*- coding: utf8 -*-

from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from gilsondev.labs.models import Project
from gilsondev.labs.forms import ProjectForm


class ProjectAdmin(AdminImageMixin, admin.ModelAdmin):
    form = ProjectForm

    def save_model(self, request, obj, form, change):
        form.save()

admin.site.register(Project, ProjectAdmin)
