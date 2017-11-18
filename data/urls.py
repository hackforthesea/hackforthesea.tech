from django.conf.urls import url, include
from django.contrib import admin

from .views import MicroshareGetDeleteView, MicroshareListCreateView

urlpatterns = [
    # GET   :recType/tags/:tag1/:tag2?details=false&page&perPage&sort
    # POST  :recType/tags/:tag1/:tag2
    url(r'^(?P<rec_type>[\.a-zA-Z]+)/tags/(?P<tags>[a-zA-Z0-9\/]+)', MicroshareListCreateView.as_view()),

    # GET   :recType/:id
    # DELETE :recType/:id
    url(r'^(?P<rec_type>[\.a-zA-Z]+)/(?P<id>[0-9a-zA-Z]+)', MicroshareGetDeleteView.as_view()),

    # POST  :recType
    # GET   :recType?details=false&page&perPage&sort
    url(r'^(?P<rec_type>[\.a-zA-Z]+)', MicroshareListCreateView.as_view()),

    # TODO: Swagger
    # url(r'^', MicroshareRelayView.as_view()),
]







