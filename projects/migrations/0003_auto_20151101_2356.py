# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20151101_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsubmission',
            name='date_started',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
