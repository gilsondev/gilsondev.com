# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('labs_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url_project', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('url_repo', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('license', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('labs', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('labs_project')


    models = {
        'labs.project': {
            'Meta': {'object_name': 'Project'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url_project': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'url_repo': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['labs']