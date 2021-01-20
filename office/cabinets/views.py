from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from cabinets.models import Seat, Reservation, Cabinet
from cabinets.permissions import IsOwnerOrReadOnly
from cabinets.serializers import SeatsSerializer, ReservationSerializer, CabinetSerializer


class SeatViewSet(ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsOwnerOrReadOnly]
    filter_fields = ['cabinet', 'reservation_time']
    search_fields = ['cabinet']


# class CabinetViewSet(ModelViewSet):
#     queryset = Cabinet.objects.all()
#     serializer_class = CabinetSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     permission_classes = [IsOwnerOrReadOnly]
#     filter_fields = ['name', 'seats']
#     search_fields = ['name']

class CabinetViewSet(ModelViewSet):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer


class UserReservationsViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    # def get_object(self):
    #     obj, _ = Reservation.objects.get_or_create(owner=self.request.user, reservation_id=self.kwargs['seat'])


def auth(request):
    return render(request, 'oauth.html')


# class UserReservationsViewSet():
#     permission_classes = [IsAuthenticated]
#     queryset = Reservation.objects.all()
#     serializer_class = ReservationSerializer
#     lookup_field = 'seat'
#
#
