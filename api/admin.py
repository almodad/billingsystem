# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class SIMCardAdmin(admin.ModelAdmin):
    list_display = ['ICCID']
admin.site.register(SIMCard, SIMCardAdmin)

class MSISDNAdmin(admin.ModelAdmin):
    list_display = ['MSISDN']
admin.site.register(MSISDNInfo, MSISDNAdmin)

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['MSISDN', 'FirstName', 'LastName']
admin.site.register(Subscriber, SubscriberAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ['MSISDN','AccountBalance']
admin.site.register(SubscriberAccount, AccountAdmin)

