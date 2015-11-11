# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='credit_offered',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='project',
            name='date_started',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='department',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='pay',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='project',
            name='supervisor',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
