# -*- coding: utf8 -*-

from django.db import models

from sorl.thumbnail import ImageField


class Project(models.Model):
    """Armazena os dados de um projeto"""
    name = models.CharField(u"Nome do Projeto", max_length=50)
    url_project = models.URLField(u"URL do Projeto")
    url_repo = models.URLField(u"URL do Repositório")
    image = ImageField(u"Imagem do Projeto", upload_to='projetos')
    license = models.CharField(u"Licença", max_length=20)

    class Meta:
        verbose_name = u"projeto"
        verbose_name_plural = u"projetos"

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        pass
