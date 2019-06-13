# -*- coding: utf-8 -*-
from rest_framework import status, urls
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.models import *
from api.serializers import *

# import the logging library
import logging
logger = logging.getLogger(__name__)
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def provisionSIM(request):
  try:
    """
    This API creates a new SIM card in the Billing system.
    """
    if request.method == 'GET':
        simcards = SIMCard.objects.all()
        serializer = SIMCardSerializer(simcards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SIMCardSerializer(data=request.data)
        #query SIMCard info
        sim = SIMCard.objects.filter(ICCID=request.data['ICCID'])
        if sim:
            logger.error('SIM already provisioned')
            return Response({"RespCode":1, "RespDesc":"SIM already provisioned"})
        else:
            if serializer.is_valid():
                if not str(request.data['ICCID']).startswith('8925402'):
                    logger.error('Invalid ICCID')
                    return Response({"RespCode":10, "RespDesc":"Invalid ICCID format"})
                elif not str(request.data['IMSI']).startswith('63902'):
                    logger.error('Invalid IMSI')
                    return Response({"RespCode":11, "RespDesc":"Invalid IMSI format"})
                else:
                    serializer.save()
                    return Response({"RespCode":0, "RespDesc":"Success"})
  except Exception, e:
      logger.error('API error')
      return Response({'RespCode':15,'RespDesc': 'API Error'})

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def activateSIM(request):
  try:
    """
    Upon receiving this API request the Billing system should 
    associate the MSISDN to an existing SIM card. If the card does not exist 
    throw an exception and return the appropriate API response. The
     status of the SIM card should be “active” after this operation is successfully invoked.
    """
    if request.method == 'GET':
        simcards = SIMCard.objects.all()
        serializer = SIMCardSerializer(simcards, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        if not str(request.data['MSISDN']).startswith('2547'):
            return Response({"RespCode":9, "RespDesc":"Invalid MSISDN"})

        sim = SIMCard.objects.filter(ICCID=request.data['ICCID'])
        if sim:
            for card in sim:
                if card.status == 1:
                    return Response({"RespCode":2, "RespDesc":"SIM already active"})
            else:
                SIMCard.objects.filter(ICCID = request.data['ICCID']).update(status=1)
                return Response({"RespCode":0, "RespDesc":"Success"})
        else:
            return Response({"RespCode":1, "RespDesc":"SIM card does not exist"})
  except Exception, e:
      return Response({'RespCode':15,'RespDesc': 'API Error'})

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def querySubscriberInfo(request):
  try:
    """
    This API queries a subscriber info using their MSISDN. This API should return the subscriber’s
    MSISDN, SIM info and the account balance.
    """
    if request.method == 'GET':
        subscribers = Subscriber.objects.all()
        serializer = SubscriberSerializer(subscribers, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        if not str(request.data['MSISDN']).startswith('2547'):
            return Response({"RespCode":9, "RespDesc":"Invalid MSISDN"})
        msisdnInfo = MSISDNInfo.objects.filter(MSISDN=request.data['MSISDN'])
        SIMInfo = list()
        accBalance = 0
        if msisdnInfo:
            #get SIM card info
            for m in msisdnInfo:
                SIMInfo = SIMCard.objects.filter(id = m.ICCID_id)
                
            accountInfo = SubscriberAccount.objects.filter(MSISDN=request.data['MSISDN'])
           
            for ac in accountInfo:
                accBalance = ac.AccountBalance
            for info in SIMInfo:
                simInfoDict = {
                                  "ICCID":info.ICCID,
                                  "Ki":info.Ki,
                                  "PIN1":info.PIN1,
                                  "IMSI":info.IMSI,
                                  "PUC":info.PUC,
                                  "status":info.status
                              }
            return Response({'MSISDN':request.data['MSISDN'],'balance':accBalance, 'SIMInfo':simInfoDict,
                'RespCode':0,'RespDesc': 'Success'})
        else:
            return Response({'RespCode':1,'RespDesc': 'MSISDN does not exist'})
  except Exception, e:
      return Response({'RespCode':15,'RespDesc': 'API Error'})

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def adjustAccountBalance(request):
  try:
    """
    This API enables an external system to adjust a subscriber’s account balance depending on the
    amount specified. A positive amount will adjust the account up and a negative amount will deduct
    from the available balance.
    """
    if request.method == 'GET':
        accounts = SubscriberAccount.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
      
        #check valis MSISDN
        if not str(request.data['MSISDN']).startswith('2547'):
            return Response({"RespCode":9, "RespDesc":"Invalid MSISDN"})
        accountInfo = SubscriberAccount.objects.filter(MSISDN=request.data['MSISDN'])
        if accountInfo:
            initialBal = 0
            for info in accountInfo:
                initialBal = info.AccountBalance
            amount = request.data['amount']
            #compute new balance
            newBalance = amount+initialBal

            SubscriberAccount.objects.filter(MSISDN=request.data['MSISDN']).update(AccountBalance=newBalance)
            return Response({'RespCode':0,'RespDesc': 'Success'})
        else:
            return Response({'RespCode':1,'RespDesc': 'MSISDN does not exist'})
  except Exception, e:
      return Response({'RespCode':15,'RespDesc': 'API Error'})

