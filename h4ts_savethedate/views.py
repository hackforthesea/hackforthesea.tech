# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView


class SaveTheDateView(TemplateView):
    template_name = "save_the_date.html"

    def get_context_data(self, **kwargs):
        context = super(SaveTheDateView, self).get_context_data(**kwargs)
        return context