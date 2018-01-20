# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import GlossaryTerm

def glossary_index(request):
    terms = GlossaryTerm.objects.all()

    return render(request, "glossary.html", { terms: terms })