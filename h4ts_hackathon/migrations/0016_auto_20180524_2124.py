# Generated by Django 2.0.5 on 2018-05-24 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('h4ts_hackathon', '0015_auto_20180524_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='note',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
