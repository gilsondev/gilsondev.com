# -*- coding: utf8 -*-

from django.db import models


class Portfolio(models.Model):
    """Armazena os dados de um portfólio"""
    nome = models.CharField(u"Nome do Projeto", max_length=50)
    url = models.URLField(u"URL do Projeto")
    imagem = models.ImageField(u"Imagem do Projeto", upload_to='portfolios')

    class Meta:
        verbose_name = u"portfólio"
        verbose_name_plural = u"portfólios"

    def __unicode__(self):
        return self.nome

    @models.permalink
    def get_absolute_url(self):
        pass
