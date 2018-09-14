"""hackforthesea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
from django.views.generic import RedirectView

import data.urls as data_urls
import core.views as core_views

from h4ts_hackathon.views import *
import hackforthesea.settings as settings

urlpatterns = [
    url(r'^accounts/login', login, {'template_name': 'admin/login.html'}),
    url(r'^accounts/logout', logout),
    url(r'^accounts/register', core_views.signup),
    
    url(r'^admin/', admin.site.urls),

    url(r'^marine-hacker-sandbox/', include('h4ts_sandbox.urls')),
    
    # 2017 Legacy Views
    # url(r'^data/', include("data.urls")),
    # url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
    # Hackathon Views
    url(r'^(?P<code>(?<![A-Z])[A-Z]{3})$', HackathonView.as_view(), name="hackathon_challenges"),
    url(r'^(?P<code>(?<![A-Z])[A-Z]{3})/apply_for_sponsorship$', ApplyForSponsorshipView.as_view(), name="hackathon_apply_for_sponsorship"),
    url(r'^(?P<code>(?<![A-Z])[A-Z]{3})/contact', ContactView.as_view(), name="hackathon_contact"),
    url(r'^(?P<code>(?<![A-Z])[A-Z]{3})/challenge/(?P<challenge_id>.*)$', ChallengeView.as_view(), name="hackathon_challenge"),
    url(r'^(?P<code>(?<![A-Z])[A-Z]{3})/FAQ$', FAQView.as_view(), name="hackathon_faq"),
    url(r'^(?P<code>(?<![A-Z])[A-Z]{3})/lodging', LodgingView.as_view(), name="hackathon_lodging"),
    url(r'^(?P<code>(?<![A-Z])[A-Z]{3})/sponsor-ticket$', SponsorTicketView.as_view(), name="hackathon_sponsor_ticket"),
    
    url(r'^', SplashView.as_view(), name="splash"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
