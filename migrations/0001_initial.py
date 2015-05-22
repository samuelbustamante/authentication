# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allowed',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=64, unique=True, verbose_name='username')),
            ],
            options={
                'verbose_name': 'usuario permitido',
                'verbose_name_plural': 'usuarios permitidos',
            },
        ),
    ]
