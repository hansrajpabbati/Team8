# Generated by Django 2.2.6 on 2019-11-03 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
