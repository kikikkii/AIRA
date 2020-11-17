from django.shortcuts import render
from . import models
from . import ticketSerializer,airplaneSerializer
from django.core import serializers
from rest_framework.views import APIView
from django.http import HttpResponse,JsonResponse
from django.db.models import Min,Count,F,Avg
import json

class directResearch(APIView):
    def get(self, request):
        dcityName = request.GET.get('dcityName')
        dtime = request.GET.get('dtime')
        query_list = models.Tickets.objects.filter(dcityName=dcityName,departureDate__date='2020-11-19')
        query_list2 = query_list.values('acity').annotate(tmin = Min('price'))
        allcities = []
        list = []
        for i in query_list2:
            for j in query_list:
                if j.price == i['tmin'] and j.acity == i['acity'] and j.acity not in allcities:
                    allcities.append(j.acity)
                    list.append(j)
        #print(query_list2)
        print("****************")
        serializer = ticketSerializer.Ticket2Serializer(list, many=True)
        return JsonResponse(serializer.data, safe=False)

class NormalResearch(APIView):
    def get(self,request):
        dcityName = request.GET.get('dcityName')
        dtime = request.GET.get('dtime')
        acityName = request.GET.get('acityName')
        query_list = models.Tickets.objects.filter(dcityName=dcityName, departureDate__date=dtime,acityName=acityName)
        serializer = ticketSerializer.Ticket2Serializer(list,many=True)
        return JsonResponse(serializer.data,safe=False)

    def post(self,request):
        print('************')
        dict = request.data
        print(type(dict))
        #dict = json.loads(postdata)
        dcity = dict.get('dcity')
        acity = dict.get('acity')
        dtime = dict.get('departureData')

        print("flightid= ",id)
        query = models.Tickets.objects.filter(dcity=dcity,acity=acity,departureDate=dtime)
        print("*******************")
        if query.count() != 0:
            for i in query:
                if i.price >= dict['price']:
                    return HttpResponse('已有数据')
                else:
                    i.update(url=dict['url'],price=dict['price'])
                    return HttpResponse('更新成功')

        serializer = ticketSerializer.Ticket2Serializer(data=dict)
        print(dict)
        if serializer.is_valid(raise_exception=True):
            print("*************************")

            serializer.save()
            return HttpResponse("OK")

class updateTicket(APIView):
    def post(self,request):
        print("this is update")
        dict = request.data
        #确定机票的航线没有重复
        ddata = dict.get('ddate') #出发日期
        dcityName = dict.get('dcityName') #出发城市
        acityName = dict.get('acityName') #到达城市
        if airplaneSerializer.airplaneSerializer.is_valid(dict):
            serializer = airplaneSerializer.airplaneSerializer(data=dict)
        serializer.save()
        print('保存成功')



#  Create your views here.