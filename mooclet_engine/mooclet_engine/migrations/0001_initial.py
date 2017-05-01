# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-25 00:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mooclet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'policies',
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(blank=True, null=True)),
                ('value', models.FloatField(blank=True, null=True)),
                ('text', models.TextField(blank=True, default='')),
                ('timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('mooclet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mooclet_engine.Mooclet')),
                ('policy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mooclet_engine.Policy')),
            ],
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('display_name', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('mooclet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mooclet_engine.Mooclet')),
            ],
        ),
        migrations.AddField(
            model_name='value',
            name='variable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mooclet_engine.Variable'),
        ),
        migrations.AddField(
            model_name='value',
            name='version',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mooclet_engine.Version'),
        ),
        migrations.AddField(
            model_name='mooclet',
            name='policy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mooclet_engine.Policy'),
        ),
    ]