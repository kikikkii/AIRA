from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from . import wx_login
from django.core.cache import cache
import hashlib, time,json
from .models import Wxuser,concernFlight
from .serializers import *


class Login(APIView):

    def post(self, request):
        param = request.data
        if not param.get('code'):
             return Response({'status':1, "msg":"缺少参数"})
        else:
            code = param.get('code')
            user_data = wx_login.get_login_info(code)
            if user_data:
                val = user_data['session_key'] + "&" + user_data['openid']
                md5 = hashlib.md5()
                md5.update(str(time.clock()).encode('utf-8'))
                md5.update(user_data['session_key'].encode('utf-8'))
                key = md5.hexdigest()
                cache.set(key, val)
                has_user = Wxuser.objects.filter(openid=user_data['openid']).first()
                if not has_user:
                    Wxuser.objects.create(openid=user_data['openid'])
                Wxuser.objects.update()
                return Response({
                    'status': 0,
                    'msg': 'ok',
                    'data': {'token':key}
                })
            else:
                return Response({'status':2, 'msg': "无效的code"})

class concernList(APIView):
    def get(self,request):
        #openid = request.GET.get("openid")
        #concernList = concernFlight.objects.filter(openid=openid)
        # 测试用
        query = Wxuser.objects.get(openid="1")
        query2 = query.concernflight_set.all()
        print(query.name)
        serializer = concernFlightSerializer(query2, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self,request):
        # 从request中获取数据
        openid = request.POST.get("openid")
        flightNumber = request.POST.get("flightNumber")
        postBody = request.body
        dict = json.loads(postBody)
        #
        query = Wxuser.models.filter(openid=openid)
        query2 = query.concernflight_set.all()
        for i in query2:
            if i.flightNumber == flightNumber:
                return HttpResponse("已收藏")
        serializer = concernFlightSerializer(data=dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        




# Create your views here.
