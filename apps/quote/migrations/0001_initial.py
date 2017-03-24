# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256)),
                ('quoted_by', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('alias', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=512)),
                ('date_of_birth', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='quote',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to='quote.User'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='quote_favorite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quote_fav', to='quote.Quote'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user_favorite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_fav', to='quote.User'),
        ),
    ]