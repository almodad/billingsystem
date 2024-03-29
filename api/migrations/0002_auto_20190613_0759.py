# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-13 07:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msisdninfo',
            name='MSISDN',
            field=models.BigIntegerField(unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 12', regex='^.{12}$')]),
        ),
        migrations.AlterField(
            model_name='simcard',
            name='ICCID',
            field=models.BigIntegerField(unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 20', regex='^.{20}$')]),
        ),
        migrations.AlterField(
            model_name='simcard',
            name='IMSI',
            field=models.BigIntegerField(validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 15', regex='^.{15}$')]),
        ),
        migrations.AlterField(
            model_name='simcard',
            name='PIN1',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 4', regex='^.{4}$')]),
        ),
        migrations.AlterField(
            model_name='simcard',
            name='PUC',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 6', regex='^.{6}$')]),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='MSISDN',
            field=models.BigIntegerField(unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 12', regex='^.{12}$')]),
        ),
        migrations.AlterField(
            model_name='subscriberaccount',
            name='MSISDN',
            field=models.BigIntegerField(unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 12', regex='^.{12}$')]),
        ),
    ]
