from rest_framework import serializers
from .models import *

class SIMCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SIMCard
        fields = ('ICCID','IMSI','Ki','PIN1','PUC')

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('MSISDN','FirstName','LastName')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriberAccount
        fields = ('MSISDN','AccountBalance')
