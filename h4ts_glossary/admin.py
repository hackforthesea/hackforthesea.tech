# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import GlossaryTerm

class GlossaryTermAdmin(admin.ModelAdmin):
    pass

admin.site.register(GlossaryTerm, GlossaryTermAdmin)