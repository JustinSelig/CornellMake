# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_auto_20151101_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default=b'username', max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('school', models.CharField(max_length=200)),
                ('major', models.CharField(max_length=200)),
                ('member_requests', models.ManyToManyField(related_name='member_requests_reverse', to='projects.Project')),
                ('projects', models.ManyToManyField(to='projects.Project')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
