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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('username', models.CharField(verbose_name='username', unique=True, max_length=30)),
            ],
            options={
                'verbose_name': 'usuario permitido',
                'verbose_name_plural': 'usuarios permitidos',
            },
            bases=(models.Model,),
        ),
    ]
