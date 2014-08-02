# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Notify'
        db.delete_table('enquiry_notify')


    def backwards(self, orm):
        # Adding model 'Notify'
        db.create_table('enquiry_notify', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('enquiry', ['Notify'])


    models = {
        'enquiry.enquiry': {
            'Meta': {'object_name': 'Enquiry', 'ordering': "['-created']"},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['enquiry']