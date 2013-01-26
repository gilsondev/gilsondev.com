# -*- coding: utf8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

from gilsondev.labs.models import Project


class ProjectModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            name='Nome do Projeto',
            url_project='http://projeto.com',
            url_repo='http://github.com/user/test',
            image='/media/projects/imagem.png',
            license='BSD'
        )

    def test_create(self):
        """O porfolio deve ser criado"""
        self.assertTrue(self.project.pk)

    def test_unicode(self):
        """Exibe a representação do objeto em String"""
        self.assertEquals(u'Nome do Projeto', unicode(self.project))


class ProjectURLTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('projects'))

    def test_get(self):
        """Retorna status 200"""
        self.assertEquals(self.resp.status_code, 200)


class ProjectViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('projects'))

    def test_use_template(self):
        """Verifica o template usado"""
        self.assertTemplateUsed(self.resp, 'labs/project_list.html')

    def test_list_in_context(self):
        """Envia a lista de porfolios no contexto da view"""
        self.assertTrue(self.resp.context.has_key('projects'))
