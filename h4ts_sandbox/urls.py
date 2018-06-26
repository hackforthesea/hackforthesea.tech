from django.conf.urls import url, include
from django.contrib import admin

from .views import SignupView

urlpatterns = [
    url(r'^$', SignupView.as_view()),
]
