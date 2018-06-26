from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import TemplateView, ListView, FormView

from .forms import SandboxSignupForm
from h4ts_hackathon.models import Purveyor


# Create your views here.

class SignupView(FormView):
    template_name = 'sandbox/signup.html'
    form_class = SandboxSignupForm
    success_url = '/marine-hacker-sandbox/?signup_success=true'

    def form_valid(self, form):
        email = self.request.POST['email']
        
        template = get_template('signup_email_template.txt')
        context = {
            'email': email
        }
        content = template.render(context)

        email = EmailMessage(
            "New Marine Hacker Sandbox Signup!",
            content,
            'mark@mrh.io',
            # "Your website" +'',
            ['henderson.mark@gmail.com'],
            # headers = {'Reply-To': contact_email }
        )
        email.send()
        return super(SignupView, self).form_valid(form)
        
    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)

        if "signup_success" in self.request.GET:
            context['signup_success'] = True
        
        context['purveyors'] = Purveyor.objects.filter(in_footer=True)
        return context
