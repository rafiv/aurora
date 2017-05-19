# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('taggit', '0002_auto_20150616_2121'),
        ('AuroraUser', '0004_auto_20170428_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('post_date', models.DateTimeField(verbose_name='date posted')),
                ('delete_date', models.DateTimeField(blank=True, null=True, verbose_name='date deleted')),
                ('edited_date', models.DateTimeField(blank=True, null=True, verbose_name='date edited')),
                ('promoted', models.BooleanField(default=False)),
                ('seen', models.BooleanField(default=False)),
                ('object_id', models.PositiveIntegerField()),
                ('visibility', models.CharField(choices=[('public', 'public'), ('staff', 'staff only'), ('private', 'private note')], default='public', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AuroraUser.AuroraUser')),
                ('bookmarked_by', models.ManyToManyField(related_name='bookmarked_comments_set', to='AuroraUser.AuroraUser')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('deleter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deleted_comments_set', to='AuroraUser.AuroraUser')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='Comments.Comment')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='CommentList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revision', models.BigIntegerField(default=0)),
                ('uri', models.CharField(max_length=200, null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='CommentReferenceObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommentsConfig',
            fields=[
                ('key', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.BooleanField(choices=[(True, True), (False, False)], default=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='Comments.Comment')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AuroraUser.AuroraUser')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('voter', 'comment')]),
        ),
        migrations.AlterUniqueTogether(
            name='commentlist',
            unique_together=set([('content_type', 'object_id')]),
        ),
    ]
