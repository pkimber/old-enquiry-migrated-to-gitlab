# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=75)),
                ('phone', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name_plural': 'Enquiries',
                'verbose_name': 'Enquiry',
            },
            bases=(models.Model,),
        ),
    ]
