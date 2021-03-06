# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from ordered_model.models import OrderedModel


class BeneficiaryOrganization(models.Model):
    name = models.CharField(max_length=512)
    logo = models.FileField(upload_to='beneficiary_logos/', null=True)
    url = models.URLField()
    
    def __str__(self):
        return self.name


class ChallengeStatement(OrderedModel):
    question = models.CharField(max_length=320)
    image = models.FileField(upload_to='challenge_imgages/', null=True)
    description = models.TextField()
    hackathon = models.ForeignKey("Hackathon", on_delete=models.CASCADE)
    beneficiaries = models.ManyToManyField(BeneficiaryOrganization, related_name='challenges')
    pass

    def __str__(self):
        return self.question
        
    class Meta(OrderedModel.Meta):
        pass


class DataSet(models.Model):
    title = models.CharField(max_length=512)
    note = models.CharField(max_length=512, null=True, blank=True)
    url = models.URLField()
    challenge = models.ManyToManyField(ChallengeStatement, related_name="datasets")

    def __str__(self):
        return self.title


class Hackathon(models.Model):
    name = models.CharField(max_length=512)
    unlocode = models.CharField(max_length=5, unique=True)
    description = models.TextField()
    ticket_link = models.URLField()
    address = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    state = models.CharField(max_length=2)
    logo = models.FileField(upload_to='hackathon_logos/', null=True)
    start_time = models.DateTimeField(default=datetime.now, blank=True)
    end_time = models.DateTimeField(default=datetime.now, blank=True)
    organizers = models.ManyToManyField(User, related_name="hackathons")

    def __str__(self):
        return self.name


class Purveyor(models.Model):
    name = models.CharField(max_length=512)
    logo = models.FileField(upload_to='sponsor_logos/', null=True)
    in_footer = models.BooleanField()
    url = models.URLField()
    
    def __str__(self):
        return self.name

    
class Team(models.Model):
    name = models.CharField(max_length=512)
    hackathon = models.ForeignKey('Hackathon', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FrequentlyAskedQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)

    def __str__(self):
        return self.question