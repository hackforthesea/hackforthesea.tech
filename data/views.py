# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from requests import get, post, delete
from hackforthesea import settings

from oauth2_provider.views.generic import ProtectedResourceView


def authentication_headers():
    url = "https://dauth.microshare.io/oauth2/token?username={}&password={}&client_id={}&grant_type=password&scope=ALL:ALL".format(
        settings.MICROSHARE_USERNAME, settings.MICROSHARE_PASSWORD, settings.MICROSHARE_API_KEY)

    response = post(url)
    json = response.json()

    token = json.get('access_token')
    headers = {
        "Authorization": "Bearer {}".format(token)
    }

    return headers

def cleantags(tags):
    if tags:
        tags = "tags/{}".format(tags)
        if tags.endswith('/'):
            tags = tags[:-1]
    return tags

class MicroshareGetDeleteView(ProtectedResourceView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MicroshareGetDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, rec_type, id):
        url = "https://dapi.microshare.io/share/{}/{}".format(rec_type, id)
        response = get(url, headers=authentication_headers())
        return JsonResponse(response.json())

    def delete(self, request, id, rec_type):
        url = "https://dapi.microshare.io/share/{}/{}".format(rec_type, id)
        response = delete(url, headers=authentication_headers())
        return JsonResponse(response.json())


class MicroshareListCreateView(ProtectedResourceView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MicroshareListCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, rec_type=None, tags=''):
        # @type boolean
        # Will return matching objects with their details, false will only return main information
        details = request.GET.get('details', "false")

        # @type int
        # Specifies the requested page, defaults to 1
        page = request.GET.get('page', 1)

        # @type int
        # Specifies the number of objects to be returned per page, defaults to 999
        perPage = request.GET.get('perPage', 999)

        # @type string
        # Specifies if sorting needs to be applied and to which field in the data
        sort = request.GET.get('sort', '')
        if sort != '':
            sort = '&sort={}'.format(sort)

        params = "?details={}&page={}&perPage={}{}".format(details,page,perPage, sort)
        url = "https://dapi.microshare.io/share/{}/{}{}".format(rec_type, cleantags(tags), params)
        response = get(url, headers=authentication_headers())
        return JsonResponse(response.json())

    def post(self, request, rec_type=None, tags=''):
        url = "https://dapi.microshare.io/share/{}/{}".format(rec_type, cleantags(tags))
        response = post(url, request.body, headers=authentication_headers())
        return JsonResponse(response.json())