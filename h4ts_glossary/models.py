# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class GlossaryTerm(models.Model):
    term = models.CharField(max_length=256)
    definition = models.TextField()
