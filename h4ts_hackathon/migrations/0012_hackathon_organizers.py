# Generated by Django 2.0.5 on 2018-05-24 19:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('h4ts_hackathon', '0011_auto_20180524_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='organizers',
            field=models.ManyToManyField(related_name='hackathons', to=settings.AUTH_USER_MODEL),
        ),
    ]