from rest_framework import serializers
from .models import Wxuser,concernFlight

class WxuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wxuser
        fields = '__all__'

class concernFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = concernFlight
        fields = '__all__'
        