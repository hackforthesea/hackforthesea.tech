from __future__ import unicode_literals

from datetime import datetime

from django.db import models


class Sponsor(models.Model):
    name = models.CharField(max_length=512)
    image_url = models.URLField(max_length=512)
    link_url = models.URLField(max_length=512)
    monetary = models.BooleanField()
    amount = models.IntegerField(null=True,blank=True)
    note = models.TextField()

    def __str__(self):
        return self.name


class CommunityPartner(models.Model):
    name = models.CharField(max_length=512)
    image_url = models.URLField(max_length=512)
    link_url = models.URLField(max_length=512)
    note = models.TextField()

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=512)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name


class Hackathon(models.Model):
    name = models.CharField(max_length=512)
    location = models.ForeignKey('Location')
    start_time = models.DateTimeField(default=datetime.now, blank=True)
    end_time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=512)
    hackathon = models.ForeignKey('Hackathon')

    def __str__(self):
        return self.name


class Participant(models.Model):
    name = models.CharField(max_length=512)
    team = models.ManyToManyField(Team)

    def __str__(self):
        return self.name


class Submission(models.Model):
    name = models.CharField(max_length=512)
    image_url = models.URLField(max_length=512)
    github_url = models.URLField(max_length=512)
    license = models.CharField
    description = models.TextField()
    team = models.ForeignKey('Team')

    def __str__(self):
        return self.name


class FrequentlyAskedQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question