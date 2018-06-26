# Generated by Django 2.0.5 on 2018-05-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeneficiaryOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('document', models.FileField(upload_to='beneficiary_logos/')),
            ],
        ),
    ]