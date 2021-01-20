import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from cabinets.models import Cabinet, Seat, Reservation
from cabinets.serializers import CabinetSerializer, SeatsSerializer


class ApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username', is_staff=True)
        self.cabinet_1 = Cabinet.objects.create(name='88', seats=4)
        self.cabinet_2 = Cabinet.objects.create(name='1', seats=4)
        self.seat_1 = Seat.objects.create(cabinet=self.cabinet_1)
        self.seat_2 = Seat.objects.create(cabinet=self.cabinet_1)
        self.seat_3 = Seat.objects.create(cabinet=self.cabinet_2)
        self.reserve_1 = Reservation.objects.create(datetime_from=datetime.now(), datetime_to=datetime.now() + timedelta(minutes=30)
                                                    ,owner=self.user, seat=self.seat_1)
        self.reserve_1 = Reservation.objects.create(datetime_from=datetime.now(),
                                                    datetime_to=datetime.now() + timedelta(minutes=60)
                                                    , owner=self.user, seat=self.seat_2)

    def test_get_cabinets(self):
        """Тест на получение данных"""
        url = 'http://127.0.0.1:8000/api/cabinet-list' #почему-то не работает reverse
        response = self.client.get(url)
        print(response)
        serializer_data = CabinetSerializer([ self.cabinet_1, self.cabinet_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_seats(self):
        """Тест на получение данных"""
        url = reverse('seat-list')
        response = self.client.get(url)
        serializer_data = SeatsSerializer([self.seat_1, self.seat_2, self.seat_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
