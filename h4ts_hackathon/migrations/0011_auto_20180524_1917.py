# Generated by Django 2.0.5 on 2018-05-24 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('h4ts_hackathon', '0010_auto_20180524_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengestatement',
            name='beneficiaries',
            field=models.ManyToManyField(related_name='challenges', to='h4ts_hackathon.BeneficiaryOrganization'),
        ),
    ]
