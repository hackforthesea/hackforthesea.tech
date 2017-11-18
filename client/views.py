# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import FrequentlyAskedQuestion

class FAQView(TemplateView):
    template_name = "faq.html"

    def get_context_data(self, **kwargs):
        context = super(FAQView, self).get_context_data(**kwargs)
        context['questions'] = FrequentlyAskedQuestion.objects.all()
        return context


class HomepageView(TemplateView):
    template_name = "homepage.html"


class SponsorsView(TemplateView):
    template_name = "sponsors.html"


class DataExploreView(TemplateView):
    template_name = "data-explore.html"