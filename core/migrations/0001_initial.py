# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('core_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('core', ['Project'])

        # Adding model 'Test'
        db.create_table('core_test', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Project'])),
            ('identifier', self.gf('django.db.models.fields.SlugField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Test'])

        # Adding model 'Testresult'
        db.create_table('core_testresult', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Test'])),
            ('testrun', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Testrun'])),
            ('error', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('resultimage', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Testresult'])

        # Adding model 'Testrun'
        db.create_table('core_testrun', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['Testrun'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('core_project')

        # Deleting model 'Test'
        db.delete_table('core_test')

        # Deleting model 'Testresult'
        db.delete_table('core_testresult')

        # Deleting model 'Testrun'
        db.delete_table('core_testrun')


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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Project']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'core.testresult': {
            'Meta': {'object_name': 'Testresult'},
            'error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resultimage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Test']"}),
            'testrun': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Testrun']"})
        },
        'core.testrun': {
            'Meta': {'object_name': 'Testrun'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['core']