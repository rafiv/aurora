# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('AuroraUser', '0002_remove_aurorauser_last_selected_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='aurorauser',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', verbose_name='Tags', through='taggit.TaggedItem', help_text='A comma-separated list of tags.'),
            preserve_default=True,
        ),
    ]
