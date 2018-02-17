# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social_Blog', '0009_auto_20180214_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review', models.IntegerField()),
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
    ]
