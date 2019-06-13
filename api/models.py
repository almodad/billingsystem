# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator

class SIMCard(models.Model):
    ICCID = models.DecimalField(max_digits=20, decimal_places=0, validators=[RegexValidator(regex='^.{20}$', 
        message='Length has to be 20', code='nomatch')], unique=True)
    IMSI = models.BigIntegerField(validators=[RegexValidator(regex='^.{15}$', 
        message='Length has to be 15', code='nomatch')])
    Ki = models.CharField(max_length = 20)
    PIN1 = models.IntegerField(validators=[RegexValidator(regex='^.{4}$', 
        message='Length has to be 4', code='nomatch')])
    PUC = models.IntegerField(validators=[RegexValidator(regex='^.{6}$', 
        message='Length has to be 6', code='nomatch')])
    status = models.SmallIntegerField(default = 0)

class Subscriber(models.Model):
    MSISDN = models.BigIntegerField(validators=[RegexValidator(regex='^.{12}$', 
        message='Length has to be 12', code='nomatch')], unique=True)
    FirstName = models.CharField(max_length = 20)
    LastName = models.CharField(max_length = 20)
    status = models.SmallIntegerField(default = 1)

class MSISDNInfo(models.Model):
    MSISDN = models.BigIntegerField(validators=[RegexValidator(regex='^.{12}$',
        message='Length has to be 12', code='nomatch')], unique=True)
    ICCID = models.ForeignKey(SIMCard, on_delete=models.CASCADE)
class SubscriberAccount(models.Model):
    MSISDN = models.BigIntegerField(validators=[RegexValidator(regex='^.{12}$',
        message='Length has to be 12', code='nomatch')], unique=True)
    AccountBalance = models.FloatField()

class SIMSwapHistory(models.Model):
    MSISDN = models.BigIntegerField(max_length = 12)
    ICCID = models.BigIntegerField(max_length = 12)
