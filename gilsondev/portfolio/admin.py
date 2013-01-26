# -*- coding: utf8 -*-

from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from gilsondev.portfolio.models import Portfolio


class PortfolioAdmin(AdminImageMixin, admin.ModelAdmin):
    pass

admin.site.register(Portfolio, PortfolioAdmin)
