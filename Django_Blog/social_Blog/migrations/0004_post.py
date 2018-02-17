# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_Blog', '0003_usercat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=255)),
                ('img', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('likes', models.IntegerField(null=True)),
                ('unLikes', models.IntegerField(null=True)),
                ('cat', models.ForeignKey(to='social_Blog.Category')),
                ('user', models.ForeignKey(to='social_Blog.User')),
            ],
        ),
    ]
