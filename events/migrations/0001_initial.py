# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'events_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.IntegerField')(default=1, null=True)),
            ('month', self.gf('django.db.models.fields.IntegerField')(default=1, null=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(default=1, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('image', self.gf('django.db.models.fields.CharField')(default='http://www.placekitten.com/200/300/', max_length=200, null=True)),
        ))
        db.send_create_signal(u'events', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'events_event')


    models = {
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'day': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "'http://www.placekitten.com/200/300/'", 'max_length': '200', 'null': 'True'}),
            'month': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True'})
        }
    }

    complete_apps = ['events']