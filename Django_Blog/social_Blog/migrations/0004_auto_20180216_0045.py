# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social_Blog', '0003_auto_20180215_0447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commmentText', models.CharField(max_length=255)),
                ('comTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ReplyComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('replyText', models.CharField(max_length=255)),
                ('repTime', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(to='social_Blog.Comment')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='unLikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='usercat',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='replycomment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postreview',
            name='post',
            field=models.ForeignKey(to='social_Blog.Post'),
        ),
        migrations.AddField(
            model_name='postreview',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='social_Blog.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
