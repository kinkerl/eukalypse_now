# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Testrun.test'
        db.add_column('core_testrun', 'test',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Test'], null=True),
                      keep_default=False)


        # Changing field 'Test.image'
        db.alter_column('core_test', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Testresult.resultimage'
        db.alter_column('core_testresult', 'resultimage', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    def backwards(self, orm):
        # Deleting field 'Testrun.test'
        db.delete_column('core_testrun', 'test_id')


        # Changing field 'Test.image'
        db.alter_column('core_test', 'image', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

        # Changing field 'Testresult.resultimage'
        db.alter_column('core_testresult', 'resultimage', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

    models = {
        'core.project': {
            'Meta': {'object_name': 'Project'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'core.test': {
            'Meta': {'object_name': 'Test'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.SlugField', [], {'max_length': '200'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'tests'", 'to': "orm['core.Project']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'core.testresult': {
            'Meta': {'object_name': 'Testresult'},
            'error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resultimage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Test']"}),
            'testrun': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Testrun']"})
        },
        'core.testrun': {
            'Meta': {'object_name': 'Testrun'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Test']", 'null': 'True'})
        }
    }

    complete_apps = ['core']