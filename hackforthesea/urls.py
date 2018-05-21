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

from beachcrab.views import beachcrabtext
import data.urls as data_urls
import core.views as core_views

from h4ts_glossary.views import glossary_index
from h4ts_hackathon.views import HackathonView
from h4ts_savethedate.views import SaveTheDateView
import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^data/', include("data.urls")),
    url(r'^accounts/login', login, {'template_name': 'admin/login.html'}),
    url(r'^accounts/logout', logout),
    url(r'^accounts/register', core_views.signup),
    url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r"^podcasts/", include("podcasting.urls")),
    url(r"^feeds/podcasts/", include("podcasting.urls_feeds")),
    url(r"^glossary/", glossary_index),
    url(r"^beachcrabtext", beachcrabtext),
    url(r'^(?P<code>)(?<![A-Z])[A-Z]{3}$', HackathonView.as_view(), name="hackathon"),
    # TODO: Gloucester -> GLO alias
    url(r'^$', SaveTheDateView.as_view(), name="home"),
    # url(r'^', include('client.urls'), name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
