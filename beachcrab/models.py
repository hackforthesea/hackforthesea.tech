# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class SMS(models.Model):
    body = models.TextField()