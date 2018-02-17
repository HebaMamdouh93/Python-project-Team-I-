# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ForbiddenWords',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=255)),
                ('wordLen', models.IntegerField()),
            ],
        ),
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
            ],
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post', models.ForeignKey(to='social_Blog.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tagName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
=======
>>>>>>> 08a132deec82ef1542a7ef806982a018ea60ce81
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userName', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('userType', models.IntegerField()),
                ('blockType', models.IntegerField()),
            ],
        ),
<<<<<<< HEAD
        migrations.CreateModel(
            name='UserCat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cat', models.ForeignKey(to='social_Blog.Category')),
                ('user', models.ForeignKey(to='social_Blog.User')),
            ],
        ),
        migrations.AddField(
            model_name='posttag',
            name='tag',
            field=models.ForeignKey(to='social_Blog.Tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(to='social_Blog.User'),
        ),
=======
>>>>>>> 08a132deec82ef1542a7ef806982a018ea60ce81
    ]
