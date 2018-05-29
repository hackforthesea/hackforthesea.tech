# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Hackathon, BeneficiaryOrganization, ChallengeStatement, FrequentlyAskedQuestion


class HackathonView(TemplateView):
    template_name = "hackathon.html"

    def get_context_data(self, **kwargs):
        context = super(HackathonView, self).get_context_data(**kwargs)
        
        context['hackathon'] = Hackathon.objects.get(unlocode=kwargs.get("code"))
        context['challenges'] = ChallengeStatement.objects.filter(hackathon=context['hackathon'])
        
        return context
        

class FAQView(TemplateView):
    template_name = "faq.html"

    def get_context_data(self, **kwargs):
        context = super(FAQView, self).get_context_data(**kwargs)
        
        context['questions'] = FrequentlyAskedQuestion.objects.all()
        
        return context
        

class ChallengeView(TemplateView):
    template_name = "challenge.html"

    def get_context_data(self, **kwargs):
        context = super(ChallengeView, self).get_context_data(**kwargs)

        context['hackathon'] = Hackathon.objects.get(unlocode=kwargs.get("code"))
        context['challenges'] = ChallengeStatement.objects.get(id=kwargs.get('id'))
        
        return context