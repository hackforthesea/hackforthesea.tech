from django.shortcuts import render

from django.views.generic import TemplateView, ListView, FormView

from .forms import SandboxSignupForm
from h4ts_hackathon.models import Purveyor


# Create your views here.

class SignupView(FormView):
    template_name = 'sandbox/signup.html'
    form_class = SandboxSignupForm
    success_url = '/'

    def form_valid(self, form):
        print(self.request.POST['nome'])
        return super(SignupView, self).form_valid(form)
        
    def get_context_data(self):
        context = super(BaseHackathonView, self).get_context_data(**kwargs)

        context['purveyors'] = Purveyor.objects.filter(in_footer=True)
        return context
