# -*- coding: utf8 -*-

from django.shortcuts import render


def list(request):
    return render(request, 'portfolio/portfolio_list.html')
