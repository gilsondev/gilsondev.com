# -*- coding: utf8 -*-

from django.test import TestCase

from gilsondev.portfolio.models import Portfolio


class PortfolioModelTest(TestCase):
    def setUp(self):
        self.portfolio = Portfolio.objects.create(
            nome='Nome do Projeto',
            url='http://projeto.com',
            imagem='/media/portfolios/imagem.png'
        )

    def test_create(self):
        """O porfolio deve ser criado"""
        self.assertTrue(self.portfolio.pk)

    def test_unicode(self):
        """Exibe a representação do objeto em String"""
        self.assertEquals(u'Nome do Projeto', unicode(self.portfolio))
