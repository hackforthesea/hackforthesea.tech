# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import SMS

@csrf_exempt
def beachcrabtext(request):
    sms = SMS()
    sms.body = json.dumps(request.POST)
    sms.save()

    # TODO Only reply once.
    message = "Thank you for submitting and cleaning up! You rock. - http://beachcrab.tech"
    twiML = '<?xml version="1.0" encoding="UTF-8"?><Response><Message><Body>{}</Body></Message></Response>'.format(message)

    response = HttpResponse(twiML)
    response["Content-Type"] = "text/xml"
    return response