# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

class HackathonView(TemplateView):
    template_name = "hackathon.html"

    def get_context_data(self, **kwargs):
        context = super(HackathonView, self).get_context_data(**kwargs)
        return context