# -*- coding: utf8 -*-

from django import forms

from gilsondev.labs.models import Project


class ProjectForm(forms.ModelForm):
    tags = forms.CharField(
        label=u"Tags",
        required=True,
        help_text=u"Separe com vígula. Ex.: projeto, python, django")

    class Meta:
        model = Project

    def save(self, commit=True):
        project = super(ProjectForm, self).save(commit=False)

        if commit:
            project.save()
            if project.tags:
                project.tags.delete()
            project.tags = self.cleaned_data['tags']

        return project
