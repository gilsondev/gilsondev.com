# -*- coding: utf8 -*-

from django.shortcuts import render

from gilsondev.portfolio.models import Portfolio


def list(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio/portfolio_list.html', {
        'portfolios': portfolios,
    })
