from rest_framework import serializers
from .models import Tickets


class Ticket2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'