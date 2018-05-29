# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import resolve
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm
from .models import Hackathon, BeneficiaryOrganization, ChallengeStatement, FrequentlyAskedQuestion, Purveyor


class BaseHackathonView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super(BaseHackathonView, self).get_context_data(**kwargs)

        context['current_url'] = resolve(self.request.path_info).url_name
        context['hackathon'] = Hackathon.objects.get(unlocode=kwargs.get("code"))
        context['challenges'] = ChallengeStatement.objects.filter(hackathon=context['hackathon'])
        context['questions'] = FrequentlyAskedQuestion.objects.all()
        context['purveyors'] = Purveyor.objects.filter(in_footer=True)
    
        if("challenge_id" in kwargs):
            context['challenge'] = ChallengeStatement.objects.get(id=kwargs.get('challenge_id'))
            context['beneficiaries'] =  context['challenge'].beneficiaries.all()
    
        return context
        

class ApplyForSponsorshipView(BaseHackathonView):
    template_name = "apply-for-sponsorship.html"

        
class ChallengeView(BaseHackathonView):
    template_name = "challenge.html"
        

class ContactView(BaseHackathonView):
    template_name = "contact.html"
    form_class = ContactForm
    
    def post(self, request, **kwargs):
        form = self.form_class(data=request.POST)
    
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                'mark@mrh.io',
                # "Your website" +'',
                ['henderson.mark@gmail.com'],
                # headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('hackathon_contact', code=kwargs.get('code'))

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        
        context['form'] = self.form_class
        context['current_url'] = resolve(self.request.path_info).url_name
        context['hackathon'] = Hackathon.objects.get(unlocode=kwargs.get("code"))

        return context
        

class FAQView(BaseHackathonView):
    template_name = "faq.html"


class HackathonView(BaseHackathonView):
    template_name = "hackathon.html"


class SponsorTicketView(BaseHackathonView):
    template_name = "sponsor-ticket.html"