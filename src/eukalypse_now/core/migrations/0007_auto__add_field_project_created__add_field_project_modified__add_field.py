# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.created'
        db.add_column('core_project', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 10, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Project.modified'
        db.add_column('core_project', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 10, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Testrun.created'
        db.add_column('core_testrun', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 10, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Testrun.modified'
        db.add_column('core_testrun', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 10, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Test.created'
        db.add_column('core_test', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 10, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Test.modified'
        db.add_column('core_test', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 10, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Testresult.created'
        db.add_column('core_testresult', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 10, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Testresult.modified'
        db.add_column('core_testresult', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 10, 11, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.created'
        db.delete_column('core_project', 'created')

        # Deleting field 'Project.modified'
        db.delete_column('core_project', 'modified')

        # Deleting field 'Testrun.created'
        db.delete_column('core_testrun', 'created')

        # Deleting field 'Testrun.modified'
        db.delete_column('core_testrun', 'modified')

        # Deleting field 'Test.created'
        db.delete_column('core_test', 'created')

        # Deleting field 'Test.modified'
        db.delete_column('core_test', 'modified')

        # Deleting field 'Testresult.created'
        db.delete_column('core_testresult', 'created')

        # Deleting field 'Testresult.modified'
        db.delete_column('core_testresult', 'modified')


    models = {
        'core.project': {
            'Meta': {'object_name': 'Project'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'core.test': {
            'Meta': {'object_name': 'Test'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.SlugField', [], {'max_length': '200'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'tests'", 'to': "orm['core.Project']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'core.testresult': {
            'Meta': {'object_name': 'Testresult'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'errorimage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'errorimage_improved': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'resultimage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Test']"}),
            'testrun': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Testrun']"})
        },
        'core.testrun': {
            'Meta': {'object_name': 'Testrun'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Project']", 'null': 'True'})
        }
    }

    complete_apps = ['core']