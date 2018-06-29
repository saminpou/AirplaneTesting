# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 23:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('description', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ActionTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.Action')),
            ],
        ),
        migrations.CreateModel(
            name='ActionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('description', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=700)),
                ('summary', models.TextField(max_length=6000)),
            ],
        ),
        migrations.CreateModel(
            name='RequestAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.Action')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.Request')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('description', models.CharField(blank=True, max_length=30)),
                ('is_complete', models.BooleanField(default=False)),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.Process')),
            ],
        ),
        migrations.CreateModel(
            name='StateType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('description', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Transition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transition_current', to='dbtest.State')),
                ('next_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transition_next', to='dbtest.State')),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.Process')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone', models.CharField(blank=True, max_length=400, null=True)),
                ('process_admin', models.ManyToManyField(to='dbtest.Process')),
            ],
        ),
        migrations.AddField(
            model_name='state',
            name='state_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.StateType'),
        ),
        migrations.AddField(
            model_name='requestaction',
            name='transition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.Transition'),
        ),
        migrations.AddField(
            model_name='request',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.User'),
        ),
        migrations.AddField(
            model_name='request',
            name='current_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.State'),
        ),
        migrations.AddField(
            model_name='request',
            name='email_list',
            field=models.ManyToManyField(related_name='transition_email', to='dbtest.User'),
        ),
        migrations.AddField(
            model_name='request',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.Process'),
        ),
        migrations.AddField(
            model_name='group',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.Process'),
        ),
        migrations.AddField(
            model_name='group',
            name='user_group',
            field=models.ManyToManyField(to='dbtest.User'),
        ),
        migrations.AddField(
            model_name='activitytarget',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.Group'),
        ),
        migrations.AddField(
            model_name='activitytarget',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.Target'),
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.ActivityType'),
        ),
        migrations.AddField(
            model_name='activity',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.Process'),
        ),
        migrations.AddField(
            model_name='actiontype',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.Process'),
        ),
        migrations.AddField(
            model_name='actiontarget',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.Group'),
        ),
        migrations.AddField(
            model_name='actiontarget',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.Target'),
        ),
        migrations.AddField(
            model_name='action',
            name='action_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.ActionType'),
        ),
        migrations.AddField(
            model_name='action',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.Process'),
        ),
        migrations.AddField(
            model_name='action',
            name='transition_action',
            field=models.ManyToManyField(to='dbtest.Transition'),
        ),
    ]