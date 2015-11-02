# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import projects.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('organization', models.CharField(max_length=100, null=True)),
                ('website', models.CharField(max_length=100, null=True)),
                ('idea_name', models.CharField(max_length=500, null=True)),
                ('description', models.TextField(default=b'default', max_length=500)),
                ('category', models.CharField(max_length=10, null=True)),
                ('image', models.FileField(default=b'Image', upload_to=projects.models.get_upload_file_name)),
                ('url', models.SlugField(max_length=200, unique=True, null=True)),
                ('member_requests', models.ManyToManyField(related_name='member_requests', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectSubmission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('organization', models.CharField(max_length=100, null=True)),
                ('website', models.CharField(max_length=100, null=True)),
                ('idea_name', models.CharField(max_length=500, null=True)),
                ('description', models.TextField(default=b'default', max_length=500)),
                ('category', models.CharField(max_length=10, null=True, choices=[(b'PT', b'Project Team'), (b'RESEARCH', b'Research'), (b'STARTUP', b'Startup'), (b'CH', b'Computer Hardware'), (b'CS', b'Computer Software'), (b'MECHE', b'Mechanical'), (b'ENV', b'Environmental'), (b'ADM', b'Art, Design, or Multimedia'), (b'SE', b'Social Entrepreneurship'), (b'OTHER', b'Other'), (b'RAND', b'Random')])),
                ('image', models.FileField(default=b'Image', upload_to=projects.models.get_upload_file_name)),
                ('url', models.SlugField(max_length=200, unique=True, null=True)),
                ('credit_offered', models.NullBooleanField()),
                ('supervisor', models.CharField(max_length=100, null=True)),
                ('pay', models.NullBooleanField()),
                ('department', models.CharField(max_length=100, null=True)),
                ('date_started', models.DateField(auto_now=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
