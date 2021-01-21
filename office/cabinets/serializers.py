from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from cabinets.models import Seat, Cabinet, Reservation


class CabinetSerializer(ModelSerializer):
    class Meta:
        model = Cabinet
        fields = ['name']


class UserSerializer(ModelSerializer):
    username = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username']


class SeatSerializer(ModelSerializer):
    cabinet = CabinetSerializer().data

    class Meta:
        model = Seat
        fields = ['cabinet']


class ReservationSerializer(ModelSerializer):
    # owner = UserSerializer()
    # seat = SeatSerializer()

    class Meta:
        model = Reservation
        fields = '__all__'


class SeatsSerializer(ModelSerializer):
    # reservation_time = ReservationSerializer()
    cabinet = CabinetSerializer()

    class Meta:
        model = Seat
        fields = ['cabinet']
