# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Enquiry.retry_count'
        db.delete_column('enquiry_enquiry', 'retry_count')

        # Deleting field 'Enquiry.email_sent'
        db.delete_column('enquiry_enquiry', 'email_sent')


    def backwards(self, orm):
        # Adding field 'Enquiry.retry_count'
        db.add_column('enquiry_enquiry', 'retry_count',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Enquiry.email_sent'
        db.add_column('enquiry_enquiry', 'email_sent',
                      self.gf('django.db.models.fields.DateTimeField')(blank=True, null=True),
                      keep_default=False)


    models = {
        'enquiry.enquiry': {
            'Meta': {'ordering': "['created']", 'object_name': 'Enquiry'},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'})
        },
        'enquiry.notify': {
            'Meta': {'object_name': 'Notify'},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'})
        }
    }

    complete_apps = ['enquiry']