# Generated by Django 2.0.5 on 2018-06-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('h4ts_hackathon', '0019_auto_20180525_1749'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='challengestatement',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='challengestatement',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
            preserve_default=False,
        ),
    ]
