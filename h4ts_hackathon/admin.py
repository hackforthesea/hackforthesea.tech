# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from ordered_model.admin import OrderedModelAdmin

from .models import *

class BeneficiaryOrganizationAdmin(admin.ModelAdmin):
    pass


class ChallengeStatementAdmin(OrderedModelAdmin):
    list_display = ('question', 'order', 'move_up_down_links')


class DataSetAdmin(admin.ModelAdmin):
    pass


class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    pass


class HackathonAdmin(admin.ModelAdmin):
    pass


class PurveyorAdmin(admin.ModelAdmin):
    pass


admin.site.register(BeneficiaryOrganization, BeneficiaryOrganizationAdmin)
admin.site.register(ChallengeStatement, ChallengeStatementAdmin)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(FrequentlyAskedQuestion, FrequentlyAskedQuestionAdmin)
admin.site.register(Hackathon, HackathonAdmin)
admin.site.register(Purveyor, PurveyorAdmin)
