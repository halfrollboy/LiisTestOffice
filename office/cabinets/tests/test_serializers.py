from datetime import datetime, timedelta
from unittest import TestCase

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from cabinets.models import Cabinet, Seat, Reservation
from cabinets.serializers import CabinetSerializer, SeatSerializer


class CabinetSerializerTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username0', is_staff=True)
        self.cabinet1 = Cabinet.objects.create(name='88', seats=25)
        self.cabinet2 = Cabinet.objects.create(name='55', seats=5)
        self.seat_1 = Seat.objects.create(cabinet=self.cabinet1)
        self.seat_2 = Seat.objects.create(cabinet=self.cabinet1)
        self.seat_3 = Seat.objects.create(cabinet=self.cabinet2)
        self.reserve_1 = Reservation.objects.create(datetime_from=datetime.now(),
                                                    datetime_to=datetime.now() + timedelta(minutes=30)
                                                    , owner=self.user, seat=self.seat_1)
        self.reserve_1 = Reservation.objects.create(datetime_from=datetime.now(),
                                                    datetime_to=datetime.now() + timedelta(minutes=60)
                                                    , owner=self.user, seat=self.seat_2)

    def test_cabinet(self):
        data = CabinetSerializer([self.cabinet1, self.cabinet2], many=True).data
        expected_data = [
            {
                'name': '88',
                'seats': 25,
            },
            {
                'name': '55',
                'seats': 5,
            }
        ]

        self.assertEqual(expected_data, data)

    def test_seats(self):
        data = SeatSerializer([self.seat_1, self.seat_2, self.seat_3], many=True).data
        # cabinet = CabinetSerializer([self.cabinet1]).data
        print(data)

        expected_data = [
            {
                'cabinet': '88'
            },
            {
                'cabinet': '88'
            },
            {
                'cabinet': '55'
            }
        ]
        self.assertEqual(expected_data, data)


