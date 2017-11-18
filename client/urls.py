from django.conf.urls import url, include
from django.contrib import admin

from views import HomepageView, DataExploreView, SponsorsView,  FAQView

urlpatterns = [
    url(r'^faq', FAQView.as_view()),
    url(r'^hackathon/', SponsorsView.as_view()),
    url(r'^sponsors', SponsorsView.as_view()),
    # url(r'^data/explore', DataExploreView.as_view()),
    url(r'^$', HomepageView.as_view()),
]
