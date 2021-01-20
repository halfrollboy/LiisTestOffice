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
    cabinet = CabinetSerializer(many=True, read_only=True)

    class Meta:
        model = Seat
        fields = ['cabinet']


class ReservationSerializer(ModelSerializer):
    owner = UserSerializer(many=True, read_only=True)
    seat = SeatSerializer(many=True, read_only=True)

    class Meta:
        model = Reservation
        fields = ['datetime_from', 'datetime_to', 'owner', 'seat']


class SeatsSerializer(ModelSerializer):
    reservation_time = ReservationSerializer(many=True, read_only=True)
    cabinet = CabinetSerializer(many=True)

    class Meta:
        model = Seat
        fields = ['id', 'cabinet', 'reservation_time']
