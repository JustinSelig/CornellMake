# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProjectSubmission'
        db.create_table(u'projects_projectsubmission', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('idea_name', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='default', max_length=500)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(default='Image', max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
        ))
        db.send_create_signal(u'projects', ['ProjectSubmission'])

        # Adding model 'Project'
        db.create_table(u'projects_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('idea_name', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='default', max_length=500)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(default='Image', max_length=100)),
        ))
        db.send_create_signal(u'projects', ['Project'])


    def backwards(self, orm):
        # Deleting model 'ProjectSubmission'
        db.delete_table(u'projects_projectsubmission')

        # Deleting model 'Project'
        db.delete_table(u'projects_project')


    models = {
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'default'", 'max_length': '500'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea_name': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'default': "'Image'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        u'projects.projectsubmission': {
            'Meta': {'object_name': 'ProjectSubmission'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'default'", 'max_length': '500'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea_name': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'default': "'Image'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        }
    }

    complete_apps = ['projects']